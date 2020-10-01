# ex83 ミニバッチ化・GPU上での学習
'''
問題82のコードを改変し，B事例ごとに損失・勾配を計算して学習を行えるようにせよ
（Bの値は適当に選べ）
．また，GPU上で学習を実行せよ．
'''

import torch
import torch.nn as nn
import pandas as pd
import numpy as np

from torch.utils.data import Dataset, TensorDataset
from torch.utils.data import DataLoader
from sklearn.feature_extraction.text import CountVectorizer

# ----------------------------------------------------------------------
# データ収集
# 1列目にカテゴリ、2列目に記事のタイトル（文章そのまま）
train = pd.read_csv('../ch08/data/train.txt', sep='\t', header=None)
valid = pd.read_csv('../ch08/data/valid.txt', sep='\t', header=None)
test = pd.read_csv('../ch08/data/test.txt', sep='\t', header=None)

# 辞書作成
vectorizer = CountVectorizer(min_df=2)
train_title = train.iloc[:,1].str.lower()
cnt = vectorizer.fit_transform(train_title).toarray()
sm = cnt.sum(axis=0)
idx = np.argsort(sm)[::-1]
words = np.array(vectorizer.get_feature_names())[idx]
dict = {}
for i in range(len(words)):
  dict[words[i]] = i+1

def get_id(sentence):
  r = []
  for word in sentence:
    r.append(dict.get(word,0))
  return r
# ----------------------------------------------------------------------

max_len = 10
# 入力次元数
dw = 300
# 隠れ層次元数
dh = 50
# 語彙数
n_vocab = len(dict) + 2
# パディング（一番最後のランク）
PAD = len(dict) + 1

class RNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.emb = nn.Embedding(n_vocab, dw, padding_idx=PAD)
        self.rnn = nn.RNN(input_size=dw, hidden_size=dh, batch_first=True)
        self.linear = nn.Linear(dh, 4)
        # self.softmax = nn.Softmax()

    def forward(self, x, h=None):
        x = self.emb(x)
        y, h = self.rnn(x, h)
        y = y[:, -1, :]
        y = self.linear(y)
        # y = self.softmax(y)
        return y

# テキストのデータフレームをidの二重リストに変換
def df2id(df):
  ids = []
  for i in df.iloc[:,1].str.lower():
    ids.append(get_id(i.split()))
  return ids

# リストをテンソルに変換
def list2tensor(data, max_len):
    new = []
    for line in data:
        if len(line) > max_len:
            line = line[:max_len]
        else:
            line += [PAD] * (max_len - len(line))
        new.append(line)
    return torch.tensor(new, dtype=torch.int64)

# 精度
def accuracy(pred, label):
    pred = np.argmax(pred.data.to('cpu').numpy(), axis=1)
    label = label.data.to('cpu').numpy()
    return (pred == label).mean()

# id化
X_train = df2id(train)
X_valid = df2id(valid)
X_test = df2id(test)

# テンソル化
X_train = list2tensor(X_train, max_len)
X_valid = list2tensor(X_valid, max_len)
X_test = list2tensor(X_test, max_len)
 
# ラベルのseries
y_train = train.iloc[:, 0]
y_valid = valid.iloc[:, 0]
y_test = test.iloc[:, 0]
# ラベル作成
category_dict = {'b': 0, 't':1, 'e':2, 'm':3}
y_train = y_train.map(lambda x: category_dict[x]).values
y_train = torch.tensor(y_train, dtype=torch.int64)
y_valid = y_valid.map(lambda x: category_dict[x]).values
y_valid = torch.tensor(y_valid, dtype=torch.int64)
y_test = y_test.map(lambda x: category_dict[x]).values
y_test = torch.tensor(y_test, dtype=torch.int64)


# ----------------------------------------------------------------------
# モデル定義
model = RNN()
# GPUの設定
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# Dataset作成
dataset = TensorDataset(X_train, y_train)
# DataLoader作成
loader = DataLoader(dataset, batch_size=1024, shuffle=True)
# 損失関数定義
loss_fn = nn.CrossEntropyLoss()
# optimizer定義
optimizer = torch.optim.SGD(model.parameters(), lr=1e-1)

epoch_num = 40
for epoch in range(epoch_num):
    for x, y in loader:
        y_pred = model(x)
        loss = loss_fn(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        y_train_pred = model(X_train.to(device))
        y_train_loss = loss_fn(y_train_pred, y_train.to(device))
        y_valid_pred = model(X_valid.to(device))
        y_valid_loss = loss_fn(y_valid_pred, y_valid.to(device))
        print('epoch', epoch, ' accuracy(train): ' , accuracy(y_train_pred, y_train), 'accuracy(valid): ', accuracy(y_valid_pred, y_valid))
    



