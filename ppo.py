from env import environment, action_space
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
import wandb
from tqdm import tqdm

# 設置模型是否使用GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

wandb.init(project="LoL Project")

# 定義每個 buff 的基礎權重
BUFF_VALUES = {
    "grubs": 20,       # 野怪 grubs
    "drake": 50,       # 小龍
    "herald": 100,     # 先鋒
    "baron": 150,      # 巴龍
    "elder": 200       # 遠古龍
}

# 更新 env 函數
def env():
    actions, allies, enemies, ally_drake_count, enemy_drake_count, ally_camp, enemy_camp, neutral_camp, grub_slain_by, current_game_seconds = environment()
    
    # 觀測值為盟友和敵方的狀態（簡單評分）
    ally_states = [ally.value for ally in allies]
    enemy_states = [enemy.value for enemy in enemies]
    game_time = [current_game_seconds]

    # 轉換 grub_slain_by 為整數
    if grub_slain_by == "Nobody":
        grub_slain_by_int = 0
    elif grub_slain_by == "enemy":
        grub_slain_by_int = -1
    else:
        grub_slain_by_int = 1
    
    # 中立資源的 Buff 與其權重（考慮是否存活 alive）
    neutral_buff_values = []
    
    for i, camp in enumerate(neutral_camp[1:], start=1):
        if camp.alive == 1:  # 當前資源存活
            if camp.buff == "grub":
                if current_game_seconds < 14 * 60:  # 14 分鐘以前
                    buff_value = BUFF_VALUES["grubs"]
                else:
                    buff_value = 0  # 14 分鐘後 grubs 不再重要
            elif camp.buff == "herald":
                if 14 * 60 <= current_game_seconds <= 20 * 60:  # 14-20 分鐘之間
                    buff_value = BUFF_VALUES["herald"]
                else:
                    buff_value = 0  # 20 分鐘後 herald 不再出現
            elif camp.buff == "drake":
                if ally_drake_count >= 3 or enemy_drake_count >= 3:  # 一方拿了三條小龍
                    buff_value = BUFF_VALUES["drake"] + 50  # 提升小龍的重要性
                else:
                    buff_value = BUFF_VALUES["drake"]
            elif camp.buff == "baron":
                buff_value = BUFF_VALUES["baron"]  # 巴龍
            elif camp.buff == "elder":
                buff_value = BUFF_VALUES["elder"]  # 遠古龍
            else:
                buff_value = 0  # 不考慮其他情況的 Buff
        else:
            buff_value = 0  # 資源不存活時權重為0
        neutral_buff_values.append(buff_value)

    # 環境的其他信息可以視作觀測值的一部分
    state = game_time + ally_states + enemy_states + [ally_drake_count, enemy_drake_count, grub_slain_by_int] + neutral_buff_values

    return state, actions

class PPOAgent(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(PPOAgent, self).__init__()
        # Actor: 負責選擇動作的神經網絡
        self.actor = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )
        
        # Critic: 評估當前狀態價值的神經網絡
        self.critic = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )
        
    def forward(self, x):
        policy_dist = self.actor(x)
        value = self.critic(x)
        return policy_dist, value

# 損失函數計算
def compute_ppo_loss(policy_dist, old_policy_dist, actions, advantages, epsilon=0.2):
    actions = actions.long().view(-1, 1)
    new_probs = policy_dist.gather(1, actions)
    old_probs = old_policy_dist.gather(1, actions)
    
    # 避免 NaN 或極端值
    new_probs = torch.clamp(new_probs, 1e-10, 1.0)
    old_probs = torch.clamp(old_probs, 1e-10, 1.0)
    
    ratio = new_probs / old_probs
    surr1 = ratio * advantages
    surr2 = torch.clamp(ratio, 1 - epsilon, 1 + epsilon) * advantages
    loss = -torch.min(surr1, surr2).mean()
    return loss


# 獎勵函數
def stochastic_reward(action, state):
    # 確定是哪個動作
    real_action = action_space[action]
    
    # 從狀態中提取玩家和敵方狀態
    ally_states = state[1:5]  # 玩家不算友軍，所以 ally 只有四個
    enemy_states = state[5:10]  # 敵方五個
    current_game_seconds = state[0]
    ally_drake_count = state[10]  # ally 拿的小龍數量
    enemy_drake_count = state[11]  # enemy 拿的小龍數量
    grub_slain_by_int = state[12]  # 這是之前定義的部分

    # 定義一個初始的獎勵值和成功概率
    reward_value = 0
    reward_probability = 0

    # 取得敵方打野的狀態分數 (enemy jungler score)
    enemy_jungler_score = enemy_states[1]  # 第二個數值為敵方打野狀態評分
    
    # 敵方打野的狀態越高，成功率越低
    jungler_influence = 1 / (1 + np.exp(0.1 * enemy_jungler_score))  # 基於敵方打野的成功率調整，打野分數越高，成功率越低
    
    # 成功率的基本計算 (基於敵我狀態的總和，但排除敵方打野)
    total_enemy_states = enemy_states.copy()
    del total_enemy_states[1]  # 移除敵方打野的評分

    total_state_diff = sum(ally_states) + sum(total_enemy_states)  # 計算排除敵方打野後的敵我實力差距
    base_probability = 1 / (1 + np.exp(-0.1 * total_state_diff))  # 這裡的0.1是平滑係數，可根據需求調整

    # 獎勵和成功率計算
    if real_action == "take grubs" and current_game_seconds < 14 * 60:
        if current_game_seconds < 9 * 60 + 45:
            reward_value = BUFF_VALUES["grubs"]
            reward_probability = base_probability * jungler_influence  # 基於敵方打野調整
        else:
            if grub_slain_by_int == 0:
                reward_value = BUFF_VALUES["grubs"] * 0.5  # 延遲奪取減少收益
                reward_probability = base_probability * jungler_influence * 0.7  # 成功率較低
            else:
                reward_value = 0  # 已被奪取，不再有價值
                reward_probability = 0

    elif real_action == "take herald" and 14 * 60 <= current_game_seconds <= 20 * 60:
        reward_value = BUFF_VALUES["herald"]
        reward_probability = base_probability * jungler_influence * 0.9  # Herald 通常對團隊戰較為重要

    elif real_action == "take drake":
        if ally_drake_count == 2 or enemy_drake_count == 2:  # 第三條龍
            reward_value = BUFF_VALUES["drake"] + 30  # 奪取第三條龍，價值提高
        elif ally_drake_count == 3 or enemy_drake_count == 3:  # 第四條龍 (龍魂)
            reward_value = BUFF_VALUES["drake"] + 100  # 龍魂，價值顯著提高
        else:
            reward_value = BUFF_VALUES["drake"]
        
        reward_probability = base_probability * jungler_influence * 0.8  # 小龍相對容易

    elif real_action == "take baron" and current_game_seconds > 20 * 60:
        reward_value = BUFF_VALUES["baron"] + (current_game_seconds - 20 * 60) // 60  # 隨時間增加價值
        reward_probability = base_probability * jungler_influence * 0.7  # 巴龍的成功率通常較低

    elif real_action == "take elder" and current_game_seconds > 20 * 60:
        reward_value = BUFF_VALUES["elder"]
        reward_probability = base_probability * jungler_influence * 0.9  # 遠古龍成功率較高，因其強化能力

    else:
        reward_value = 10  # 其他動作，如入侵敵方野區或清理自己野區
        reward_probability = base_probability * jungler_influence * 0.7  # 這些行為的成功率相對不高

    reward_value = torch.tensor(reward_value).float()  # 將 reward_value 轉換為浮點數張量
    reward_value = torch.clamp(reward_value, -1000, 1000)  # 避免極端值
    

    # 最終獎勵值為 獎勵值 * 成功率
    return reward_value * reward_probability



class PPOTrainer:
    def __init__(self, state_dim, action_dim, lr=1e-4):
        self.agent = PPOAgent(state_dim, action_dim).to(device)
        self.optimizer = optim.Adam(self.agent.parameters(), lr=lr)

    def train_step(self, states, actions, rewards, old_policy_dist, advantages):
        policy_dist, values = self.agent(states)
        
        # 將 actions 的形狀從 [batch_size] 擴展為 [batch_size, 1]
        actions = actions.unsqueeze(1)
        
        # 計算PPO損失
        ppo_loss = compute_ppo_loss(policy_dist, old_policy_dist, actions, advantages)
        
        # Critic的價值損失
        value_loss = ((values - rewards) ** 2).mean()
        
        # 總損失
        loss = ppo_loss + 0.5 * value_loss

        # 優化
        self.optimizer.zero_grad()
        loss.backward()
        # for name, param in self.agent.named_parameters():
        #     if param.grad is not None:
        #         print(f"Grad of {name}: {param.grad}")

        self.optimizer.step()

        return ppo_loss.item(), value_loss.item()


# 假設一些隨機的狀態、動作和獎勵來進行訓練
def train_model():
    trainer = PPOTrainer(state_dim=18, action_dim=8)
    for episode in tqdm(range(1000000), desc="Training Progress"):
        state, actions = env()  # 獲取當前環境狀態和可行動作
        
        if len(actions) == 0:
            print(f"No valid actions at episode {episode}")
            continue  # 如果沒有動作，跳過這次訓練迴圈
        
        states = torch.FloatTensor(state).unsqueeze(0).to(device)

        # 確保 action_indices 在 actions 的範圍內
        action_indices = torch.randint(0, len(actions), (1,)).to(device)

        # 模擬獎勵與優勢估計
        selected_action = actions[action_indices.item()]  # 根據 action_indices 選擇動作
        rewards = stochastic_reward(selected_action, state)
        rewards = torch.FloatTensor([rewards]).to(device)
        
        # 生成舊的策略分佈（模擬）
        old_policy_dist, _ = trainer.agent(states)
        
        advantages = rewards - trainer.agent.critic(states)  # 優勢估計

        ppo_loss, value_loss = trainer.train_step(states, action_indices, rewards, old_policy_dist, advantages)

        # 記錄至 wandb
        wandb.log({
            "ppo_loss": ppo_loss,
            "value_loss": value_loss,
            "reward": rewards.item(),
            "episode": episode
        })

    wandb.finish()

train_model()