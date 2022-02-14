import gym
import numpy as np
import torch

import qlearning
import ddpg
import ppo
import reinforce
import a2c
import dqn


env = gym.make('CartPole-v1')
model = qlearning.QAgent()


obs = env.reset()
for i in range(1000):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
      obs = env.reset()