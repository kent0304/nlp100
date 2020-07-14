# ex81 RNNによる予測
import torch
import torch.nn as nn
import pandas as pd

from torch.utils.data import Dataset
from torch.utils.data import DataLoader

from ex80 import encode_sentence
from ex80 import dict

# one-hot を作る関数
def id2onehot(id):
    tensor = torch.zeros(1,len(dict))
    tensor[0][id] = 1
    return tensor


class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        # torch.catでdim=1なら横に結合、0なら縦に結合
        combined = torch.cat((input, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i20(combined)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)

class MyDataset(Dataset):
    def __init__(self, x, y, encode_sentence):
        self.x = x
        self.y = y
        self.encode_sentence = encode_sentence

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        text = self.x[idx]
        inputs = self.encode_sentence(text)
        return  {
            'inputs': torch.tensor(inputs, dtype=torch.int64),
            'labels': torch.tensor(self.y[idx], dtype=torch.int64)
        }

# データ収集
# 1列目にカテゴリ、2列目に記事のタイトル（文章そのまま）
train = pd.read_csv('../ch08/data/train.txt', sep='\t', header=None)
valid = pd.read_csv('../ch08/data/valid.txt', sep='\t', header=None)
test = pd.read_csv('../ch08/data/test.txt', sep='\t', header=None)
# 記事タイトルのseries
x_train = train.iloc[:, 1]
x_valid = valid.iloc[:, 1]
x_test = test.iloc[:, 1]
# ラベルのseries
y_train = train.iloc[:, 0]
y_valid = valid.iloc[:, 0]
y_test = test.iloc[:, 0]
# ラベル作成
category_dict = {'b': 0, 't':1, 'e':2, 'm':3}
y_train = y_train.map(lambda x: category_dict[x]).values
y_valid = y_valid.map(lambda x: category_dict[x]).values
y_test = y_test.map(lambda x: category_dict[x]).values

# Datasetの作成
dataset_train = MyDataset(x_train, y_train, encode_sentence)
dataset_valid = MyDataset(x_valid, y_valid, encode_sentence)
dataset_test = MyDataset(x_test, y_test, encode_sentence)

print(dataset_train[2]['inputs'])

# パラメータの設定


model = RNN(len(dict), 128, 4)
print(model(dataset_train[2]['inputs'], 128))
#
# # since the last layer of the RNN is nn.LogSoftmax
# criterion = nn.NLLLoss()
#
# learning_rate = 0.005
#
# def train():
#     hidden = rnn.initHidden()
#     rnn.zero_grad()
#
#     for i in range(id2onehot.size()[0])
