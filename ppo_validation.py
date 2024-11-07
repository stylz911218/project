# ppo_validation.py
import torch
import numpy as np
from env import action_space
from ppo import PPOAgent, env  # 確保這些匯入與 `ppo.py` 文件一致

# 設定模型是否使用 GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加載訓練好的模型
state_dim = 18
action_dim = 8
model = PPOAgent(state_dim, action_dim).to(device)
model.load_state_dict(torch.load("trained_ppo_model.pth", weights_only=True))
model.eval()  # 設置模型為驗證模式

def decompose_state(state):
    # 解析 state 列表的結構
    current_game_seconds = state[0]
    ally_states = state[1:5]  # 盟友狀態，4 個元素
    enemy_states = state[5:10]  # 敵方狀態，5 個元素
    ally_drake_count = state[10]
    enemy_drake_count = state[11]
    grub_slain_by_int = state[12]
    neutral_buff_values = state[13:]  # 中立資源的 Buff 權重

    # 還原 grub_slain_by 的原始值
    if grub_slain_by_int == 0:
        grub_slain_by = "Nobody"
    elif grub_slain_by_int == -1:
        grub_slain_by = "enemy"
    else:
        grub_slain_by = "ally"
    
    # 將結果以字典形式返回，便於查看
    return {
        "current_game_seconds": current_game_seconds,
        "ally_states": ally_states,
        "enemy_states": enemy_states,
        "ally_drake_count": ally_drake_count,
        "enemy_drake_count": enemy_drake_count,
        "grub_slain_by": grub_slain_by,
        "neutral_buff_values": neutral_buff_values
    }


# 驗證函數
def validate_model(num_steps=1):
    for step in range(num_steps):
        # 獲取環境的當前狀態和可用的動作
        state, actions = env()
        state_tensor = torch.FloatTensor(state).unsqueeze(0).to(device)

        # 模型選擇的動作
        with torch.no_grad():
            policy_dist, _ = model(state_tensor)
            chosen_action_idx = torch.argmax(policy_dist).item()
        
        decomposestate = decompose_state(state=state)
        # 顯示結果
        print(f"Step {step + 1}")
        print(f"State: {decomposestate}")
        print(f"Available actions: {actions}")
        print(f"Chosen action by model: {action_space[actions[chosen_action_idx]]}")
        print("-" * 30)

# 執行驗證
if __name__ == "__main__":
    validate_model(num_steps=1)