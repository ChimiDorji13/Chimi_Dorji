import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode="human")

print(f"Action Space: {env.action_space}")
#The action space is Discrete(4). This means there are 4 possible actions:
#0 = Left, 1 = Down, 2 = Right, 3 = Up.
print(f"Observation Space: {env.observation_space}")
# For FrozenLake, the observation space is Discrete(16).
# This means there are 16 possible states (a 4x4 grid).
# Each number from 0 to 15 corresponds to a different square on the frozen lake.

# --- THE MAIN LOOP ---


observation, info = env.reset()

terminated = False
truncated = False
total_reward = 0.0


while not terminated and not truncated:

    env.render()

    action = env.action_space.sample()
    print(f"Taking action: {action} (0:L, 1:D, 2:R, 3:U)")

    next_observation, reward, terminated, truncated, info = env.step(action)


    total_reward += reward
    observation = next_observation


    time.sleep(5)
print(f"\nEpisode finished! Total Reward: {total_reward}")


env.close()
# In FrozenLake, the reward = 1.0 only when the agent reaches the goal (G).
# Otherwise, every step has a reward of 0.0.
# So the reward represents whether the goal was reached.