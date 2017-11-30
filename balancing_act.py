import gym
import numpy as np


env = gym.make('CartPole-v0')

print(env.action_space)
print(env.observation_space)

env.reset()
"""
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.reset()
"""

### Random Search ###

def run_episode(env, parameters):
    observation = env.reset()
    # for every timestep we keep the pole straight, get +1 reward
    total_reward = 0
    for _ in range(200):
        env.render()
        # print(observation)
        action = 0 if np.matmul(parameters, observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            break
    return total_reward

# now, select parameters to receive the highest amount of average reward

best_parameters = None
best_reward = 0
ep_no = 0
for _ in range(10000):
    parameters = np.random.rand(4) * 2 - 1
    reward = run_episode(env, parameters)
    ep_no += 1
    if reward > best_reward:
        best_reward = reward
        best_parameters = parameters
        if reward == 200:
            print('woot! after {} episodes'.format(ep_no))
            break


### Hill Climbing ###


