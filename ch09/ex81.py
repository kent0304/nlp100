# ex81 RNNによる予測
'''
ID番号で表現された単語列x=(x1,x2,…,xT)がある．
ただし，Tは単語列の長さ，xt∈ℝVは単語のID番号のone-hot表記である（Vは単語の総数である）．
再帰型ニューラルネットワーク（RNN: Recurrent Neural Network）を用い，
単語列xからカテゴリyを予測するモデルとして，次式を実装せよ．
'''

import torch
import torch.nn as nn
import pandas as pd

from torch.utils.data import Dataset
from torch.utils.data import DataLoader

from ex80 import encode_sentence
from ex80 import dict

# 入力ベクトルの次元数
dw = 300
# 隠れ状態の次元数
dh = 50

class RNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.emb = nn.Embedding(len(dict) + 1, dw)
        self.rnn = nn.RNN(input_size=dw, hidden_size=dh, batch_first=True)
        self.linear = nn.Linear(dh, 4)
        self.softmax = nn.Softmax()

    def forward(self, x, h=None):
        x = self.emb(x)
        y, h = self.rnn(x, h)
        y = y[:, -1, :] # 最後のステップ
        y = self.linear(y)
        y = self.softmax(y)
        return y

model = RNN()

print(model(torch.tensor([[146, 2969, 996, 2856, 4934, 1, 0, 0]])))




# # one-hot を作る関数
# def id2onehot(id):
#     tensor = torch.zeros(1,len(dict)+1)
#     tensor[0][id] = 1
#     return tensor


# class RNN(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(RNN, self).__init__()
#         self.hidden_size = hidden_size
#         selfep='\t', header=None)
# # 記事タイトルのseries
# x_train = train.iloc[:, 1]
# x_valid = valid.iloc[:, 1]
# x_test = test.iloc[:, 1]
# # ラベルのseries
# y_train = train.iloc[:, 0]
# y_valid = valid.iloc[:, 0]
# y_test = test.iloc[:, 0]
# # ラベル作成
# category_dict = {'b': 0, 't':1, 'e':2, 'm':3}
# y_train = y_train.map(lambda x: category_dict[x]).values
# y_valid = y_valid.map(lambda x: category_dict[x]).values
# y_test = y_test.map(lambda x: category_dict[x]).values

# # Datasetの作成
# dataset_train = MyDataset(x_train, y_train, encode_sentence)
# dataset_valid = MyDataset(x_valid, y_valid, encode_sentence)
# dataset_test = MyDataset(x_test, y_test, encode_sentence)

# print(dataset_train[2]['inputs'])

# # パラメータの設定


# model = RNN(len(dict), 128, 4)
# print(model(dataset_train[2]['inputs'], 128))
# #
# # # since the last layer of the RNN is nn.LogSoftmax
# # criterion = nn.NLLLoss()
# #
# # learning_rate = 0.005
# #
# # def train():
# #     hidden = rnn.initHidden()
# #     rnn.zero_grad()
# #
# #     for i in range(id2onehot.size()[0])
# .i2h = nn.Linear(input_size + hidden_size, hidden_size)
#         self.i2o = nn.Linear(input_size + hidden_size, output_size)
#         self.softmax = nn.LogSoftmax(dim=1)

#     def forward(self, input, hidden):
#         # torch.catでdim=1なら横に結合、0なら縦に結合
#         combined = torch.cat((input, hidden), 1)
#         hidden = self.i2h(combined)
#         output = self.i2o(combined)
#         output = self.softmax(output)
#         return output, hidden

#     def initHidden(self):
#         return torch.zeros(1, self.hidden_size)

# class MyDataset(Dataset):
#     def __init__(self, x, y, encode_sentence):
#         self.x = x
#         self.y = y
#         self.encode_sentence = encode_sentence

#     def __len__(self):
#         return len(self.y)

#     def __getitem__(self, idx):
#         text = self.x[idx]
#         inputs = self.encode_sentence(text)
#         return  {
#             'inputs': torch.tensor(inputs, dtype=torch.int64),
#             'labels': torch.tensor(self.y[idx], dtype=torch.int64)
#         }

# # データ収集
# # 1列目にカテゴリ、2列目に記事のタイトル（文章そのまま）
# train = pd.read_csv('../ch08/data/train.txt', sep='\t', header=None)
# valid = pd.read_csv('../ch08/data/valid.txt', sep='\t', header=None)
# test = pd.read_csv('../ch08/data/test.txt', s