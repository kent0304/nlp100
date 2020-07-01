import numpy as np
import pandas as pd
import torch.nn as nn
import torch

input_data = pd.read_csv('data/X_train.txt',sep=' ', header=None)
# prepare features
x1 = input_data.iloc[0, :]
x1_4 = input_data.iloc[0:4, :]
# convert pandas df to tensor
x1 = torch.tensor(x1.values, dtype=torch.float)
x1_4 = torch.tensor(x1_4.values, dtype=torch.float)



class NN(nn.Module):
    def __init__(self, input=300, output=4):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input, output, bias=False)
        nn.init.normal_(self.fc1.weight, mean=0.0, std=1.0) # 正規分布で重みを初期化

    def forward(self, x):
        return self.fc1(x)

model = NN()

y1 = torch.softmax(model.forward(x1), dim=-1)
print(y1)
y1_4 = torch.softmax(model.forward(x1_4), dim=-1)
print(y1_4)
