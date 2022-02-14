import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack =nn.Sequential(
          nn.Linear(input_size, 64),
          nn.ReLU(),
          nn.Linear(64,64),
          nn.ReLU(),
          nn.Linear(64, output_size)
        )
        self.learning_rate = 0.0005

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits