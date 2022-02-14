import numpy as np
import torch
import torch.nn as nn
import gym
import neuralnet

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class ReinAgent:
    def __init__(self, state_size, action_size) -> None:
        self.action_space = action_size
        self.state_space = state_size
        self.policy = self.make_neural_net()
        self.gamma = 0.99
        self.actions = []
        self.states = []
        self.rewards = []

    def make_neural_net(self):
        return neuralnet.NeuralNetwork(self.state_space, self.action_space)

    def choose_action(self, state):
        probs = self.policy(state)
        action = np.random.choice(self.action_space, p=probs)
        return action