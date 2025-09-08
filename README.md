Name:
Student number:


Q.A brief summary of the tasks you completed.
Ans=>I attempt to run CartPole-v1 environment in this exercise. The initial step is first importing gymnasium and getting the environment ready.Then, resetting, to get the first observation. Then I have a loop in which I choose some random action with env.action space.sample and with env. step action. I print the values of the observation, reward and the done values. Lastly I seal the environment. The pole and cart move automatically, though it is arbitrary because I did not apply any agent.as in excercise 2 I investigate what is in the observation space and action space. I can print them with print(env.observation_space) and print(env.action space). Continuous quantities such as cart position, velocity, pole angle and velocity are observed in observation space. The action space is Discrete(2) hence it is left or right only. I also attempt env.observation.space.sample and env.action.space.sample to view the example values. This assists me to understand what the agent is capable of viewing and what it is capable of performing.


Q.The answers to the questions from Exercise 1 about the CartPole environment's action and observation spaces.
Ans=>The action space is Discrete(2).This means there are exactly 2 possible actions:
0 = Push the cart to the left
1 = Push the cart to the right
The observation space is a continuous space represented by Box(4,).


Q.The final average reward you calculated for the random agent in Exercise 2.
Average reward over 1000 episodes: 0.0100





Q.A section on challenges: What was the most difficult part of this practical for you? (e.g., setting up the environment, understanding the step function's return values, structuring the loops).
Ans=>In the course of this practical I not only have some issues. To start with, upon importation of gymnasium I get error due to improper installation of the package. It worked after pip installing gymnasium. Another issue was when render=human, window not open or close quickly and I needed to restart kernel. It was also not much clear to determine what are the values of observation because they are numbers though I do not know which is position or angel. It was also difficult to read all the print outs that were produced by running the loop.


Q.A section on key takeaways: What is the most important or surprising thing you learned?
Ans=>This practicum teaches me how the two work together in the gymnasium.I understand the distinction between observation space and action space, and how the envirament is updated, step by step. With basic erring, I viewed the fundamental concept of the reinforcement learning.
