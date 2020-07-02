# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import torch.nn as nn
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from matplotlib import pyplot as plt
import time

# 学習データ用意
x_train = pd.read_csv('data/X_train.txt',sep=' ', header=None)
x_valid = pd.read_csv('data/X_valid.txt',sep=' ', header=None)
x_test = pd.read_csv('data/X_test.txt',sep=' ', header=None)
# convert pandas df to tensor
x_train = torch.tensor(x_train.values, dtype=torch.float)
x_valid = torch.tensor(x_valid.values, dtype=torch.float)
x_test = torch.tensor(x_test.values, dtype=torch.float)

# 教師ラベル用意
y_train = pd.read_csv('data/y_train.txt', header=None)
y_valid = pd.read_csv('data/y_valid.txt', header=None)
y_test = pd.read_csv('data/y_test.txt', header=None)
# convert pandas df to tensor
y_train = torch.tensor(y_train.values, dtype=torch.long).flatten()
y_valid = torch.tensor(y_valid.values, dtype=torch.long).flatten()
y_test = torch.tensor(y_test.values, dtype=torch.long).flatten()


class NN(nn.Module):
    def __init__(self, input_num=300, mid_num=150, output_num=4):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input_num, mid_num, bias=False)
        self.fc2 = nn.Linear(mid_num, mid_num, bias=False)
        self.fc3 = nn.Linear(mid_num, output_num, bias=False)

        # nn.init.normal_(self.fc1.weight, mean=0.0, std=1.0) # 正規分布で重みを初期化

    def forward(self, x):
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# データセットの作成
class MyDataset(Dataset):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __len__(self):
        return len(self.y)

    # インデックスidxで返り値指定
    def __getitem__(self, idx):
        return [self.x[idx], self.y[idx]]

# define accuracy
def calculate_loss_and_accuracy(model, loss_function, loader):
    model.eval()
    loss = 0.0
    correct = 0
    cnt = 0
    with torch.no_grad():
        for inputs, labels in loader:
            outputs = model.forward(inputs)
            loss += loss_function(outputs, labels).item()
            pred = torch.argmax(outputs, dim=-1)
            correct += (pred == labels).sum().item()
            cnt += len(inputs)

    return loss / len(loader), correct / cnt

def train_model(dataset_train, dataset_valid, batch_size, model, loss_function, optimizer, num_epochs, device=None):
    # GPUにおくる
    # model.to(device)

    # Prepare DataLoader
    dataloader_train = DataLoader(dataset_train, batch_size=batch_size, shuffle=True)
    dataloader_valid = DataLoader(dataset_valid, batch_size=len(dataset_valid), shuffle=False)
    # dataloader_test = DataLoader(dataset_test, batch_size=len(dataset_test), shuffle=False)

    # Training
    log_train = []
    log_valid = []
    for epoch in range(num_epochs):
        # 開始時刻の記録
        s_time = time.time()
        # start training
        model.train()
        loss_train = 0.0
        for i, (inputs, labels) in enumerate(dataloader_train):
            # 勾配をゼロで初期化
            optimizer.zero_grad()

            # 順伝播 + 誤差逆伝播 + 重み更新
            outputs = model.forward(inputs)
            loss = loss_function(outputs, labels)
            loss.backward()
            optimizer.step()

        # calculate accuracy
        loss_train, acc_train = calculate_loss_and_accuracy(model, loss_function, dataloader_train)
        loss_valid, acc_valid = calculate_loss_and_accuracy(model, loss_function, dataloader_valid)
        log_train.append([loss_train, acc_train])
        log_valid.append([loss_valid, acc_valid])

        # save checkpoints
        torch.save({'epoch': epoch, 'model_state_dict': model.state_dict(), 'optimizer_state_dict': optimizer.state_dict()}, f'checkpoints/checkpoint{epoch+1}.pt')
        # 終了時刻の記録
        e_time = time.time()
        # output logs
        print(f'epoch: {epoch + 1}, loss_train:{loss_train:.4f}, acc_train:{acc_train:.3f}, loss_valid:{loss_valid:.4f}, acc_valid:{acc_valid:.3f}, {(e_time - s_time):.4f}sec')
        # 検証データの損失が3エポック連続で低下しなかった場合は学習終了
        if epoch > 2 and log_valid[epoch - 3][0] <= log_valid[epoch - 2][0] <= log_valid[epoch - 1][0] <= log_valid[epoch][0]:
          break
    return {'train': log_train, 'valid': log_valid}


# define a model
model = NN()
# define a loss function
loss_function = nn.CrossEntropyLoss()
# define a optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

# Prepare Dataset
dataset_train = MyDataset(x_train, y_train)
dataset_valid = MyDataset(x_valid, y_valid)
dataset_test = MyDataset(x_test, y_test)

# デバイスの指定
# device = torch.device('cuda')

# training a model
log = train_model(dataset_train, dataset_valid, 64, model, loss_function, optimizer, num_epochs=1000, device=0)
# for batch_size in [2**i for i in range(11)]:
#     print(f'バッチサイズ: {batch_size}')
#     log =  train_model(dataset_train, dataset_valid, batch_size, model, loss_function, optimizer, 1, device = 0)

# visualization
fig, ax = plt.subplots(1,2, figsize=(15,5))
ax[0].plot(np.array(log['train']).T[0], label='train')
ax[0].plot(np.array(log['valid']).T[0], label='valid')
ax[0].set_xlabel('epoch')
ax[0].set_ylabel('loss')
ax[0].legend()
ax[1].plot(np.array(log['train']).T[1], label='train')
ax[1].plot(np.array(log['valid']).T[1], label='valid')
ax[1].set_xlabel('epoch')
ax[1].set_ylabel('accuracy')
ax[1].legend()
plt.show()
