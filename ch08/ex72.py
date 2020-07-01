import numpy as np
import pandas as pd
import torch.nn as nn
import torch

input_data = pd.read_csv('data/X_train.txt',sep=' ', header=None)
# prepare features
x1 = input_data.iloc[:1, :]
x1_4 = input_data.iloc[0:4, :]
# convert pandas df to tensor
x1 = torch.tensor(x1.values, dtype=torch.float)
x1_4 = torch.tensor(x1_4.values, dtype=torch.float)


# 教師ラベル用意
label_data = pd.read_csv('data/y_train.txt', header=None)
y1 = label_data.iloc[:1, :]
y1_4 = label_data.iloc[0:4, :]
# convert pandas df to tensor
y1 = torch.tensor(y1.values, dtype=torch.long).flatten()
y1_4 = torch.tensor(y1_4.values, dtype=torch.long).flatten()
# print(y1)
# print(y1_4)



class NN(nn.Module):
    def __init__(self, input=300, output=4):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input, output, bias=False)
        nn.init.normal_(self.fc1.weight, mean=0.0, std=1.0) # 正規分布で重みを初期化

    def forward(self, x):
        return self.fc1(x)

model = NN()

# print(model.forward(x1))
# print(y1)
loss = nn.CrossEntropyLoss()
output_1 = loss(model.forward(x1),y1)
model.zero_grad()
output_1.backward()

print('損失(x1)', output_1.item())
print('勾配(x1)', model.fc1.weight.grad)

loss = nn.CrossEntropyLoss()
output_14 = loss(model.forward(x1_4),y1_4)
model.zero_grad()
output_14.backward()

print('損失(x1-4)', output_14.item())
print('勾配(x1-4)', model.fc1.weight.grad)
