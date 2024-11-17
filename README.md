2023-2024 NTHU Grade 3-4 Project
===
# Reinforcement Learning in League of Legends

**Author**: Po-Sheng, Yang
**Student ID**: 110062342  
**University**: Computer Science, National Tsing Hua University

---

## Abstract
This study applies reinforcement learning (RL) to develop an intelligent decision-making agent for *League of Legends* (LoL). Using Proximal Policy Optimization (PPO), we trained a jungle-role agent to deliver strategic recommendations in real-time. Validation against expert analysis showed strong alignment in early to mid-game decisions, with challenges in late-game prioritization. Findings highlight potential overfitting in longer training episodes, offering insights for improving AI-based decision support in gaming.

---

## I. Introduction
Esports, particularly *LoL*, presents a complex environment ideal for testing RL applications. By working with ex-esports analysts, we compiled a dataset of in-game statistics and strategies to train our RL models. This project uses a Stochastic Reward Machine (SRM) to capture the game’s randomness, with PPO handling the high-dimensional decision space, aiming to develop an intelligent jungle-role agent.

---

## II. Motivation
Inspired by years of experience in *LoL*, I explored RL to create tools aiding in real-time decision-making for jungle players. This model has broader implications for testing RL algorithms in complex, stochastic settings, combining personal passion for gaming with academic RL principles to contribute meaningfully to both fields.

---

## III. Methodology
Our approach is divided into two main components: **Environment Implementation** and **Model Development**.

### 1. Environment Implementation
Key components include:
- **Jungle Camp**: Divided into sections with varying objectives (e.g., Drake, Baron).
- **Champion Modeling**: Tracking stats, positioning, and team roles.
- **Scene Preparation**: Randomized game scenarios to capture diverse in-game states.
- **Game Mechanics**: Strategic zone values and champion behaviors.

### 2. Model Development
Using PPO, the model consists of actor and critic networks:
- **Actor Network**: Selects actions based on game state.
- **Critic Network**: Assesses state values, guiding decisions.
- **Reward Function**: Balances high-value and risky actions, considering probabilistic influences.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b8a7dc89-c970-4bd6-b3ad-1a0efc02dfec" alt="PPO Model Architecture">
</p>

<p align="center"><b>PPO Model Architecture</b></p>

<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/a67fc3a4-f61f-422c-ac35-620017d15ed8" alt="Reward Function">
</p>

<p align="center"><b>Reward Function</b></p>

---

## IV. Experiment

### 1. Training Results
We analyzed six training runs:
- **Reward Performance**: Shorter training (4 million episodes) led to faster stabilization, while longer training (10 million episodes) improved reward consistency.
- **PPO and Value Loss**: All models converged around similar loss levels, with early stability in shorter-trained models.
![image](https://github.com/user-attachments/assets/9978b651-c461-460a-8c15-c29f32778461)

### 2. Validation
Comparing model decisions to human judgments revealed high agreement in early/mid-game but divergence in late-game scenarios. Metrics included:
- **Decision Alignment Rate**: Comparison with expert and personal judgments.
- **Temporal Analysis**: Alignment breakdown across game phases.
- **Strategic Depth**: Assessment of model decisions in complex situations.

<p align="center">
  <img src="https://github.com/user-attachments/assets/79a2403c-9442-4d73-afbd-bf9e00cc5971" alt="Including 'Human hard to Judge' + 1000-million-episode model">
</p>

<p align="center"><b>Including "Human hard to Judge" + 1000-million-episode model</b></p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/9a6a513f-8bdc-41b0-93bf-3e2968f34385" alt="Excluding 'Human hard to Judge' + 1000-million-episode model">
</p>

<p align="center"><b>Excluding "Human hard to Judge" + 1000-million-episode model</b></p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/3b0453c0-b428-4371-9f0c-76f629ce2bdf" alt="Including 'Human hard to Judge' + 400-million-episode model">
</p>

<p align="center"><b>Including "Human hard to Judge" + 400-million-episode model</b></p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/6fa1b672-61d9-4a97-aea0-1edcb8b23d9c" alt="Excluding 'Human hard to Judge' + 400-million-episode model">
</p>

<p align="center"><b>Excluding "Human hard to Judge" + 400-million-episode model</b></p>


---

## V. Conclusions & Discussion
- **4 Million Episodes Outperform**: Shorter training generally led to better decision-making accuracy.
- **Challenges in Late Game**: Lower agreement in late-game highlights the need for nuanced decision-making.
- **Early Game Success**: Simpler objectives may explain better early-game performance.

---

## VI. Future Work
1. **Enhanced Environment Complexity**: Incorporate more game dynamics (e.g., cooldowns, vision control).
2. **Improved Decision-Making**: Explore multi-agent reinforcement learning to align with high-level play.
3. **Role Expansion**: Adapt model for other roles beyond jungle to provide team-wide support.

---

## References
1. Corazza, J., Gavran, I., & Neider, D. *Reinforcement Learning with Stochastic Reward Machines*, AAAI Technical Track on Machine Learning I, 2022.
2. Gullapalli, V. *A Stochastic Reinforcement Learning Algorithm for Learning Real-Valued Functions*, *Neural Networks*, 1990.
3. Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. *Proximal Policy Optimization Algorithms*, 2017.

---

