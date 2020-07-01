import chainer
import numpy as np
import pandas as pd
import chainer.links as L
import chainer.functions as F
from chainer import Variable

# 特徴量用意
train_data = pd.read_csv('data/X_train.txt',sep=' ', header=None)
x1_4 = train_data.iloc[0:4, :]
# float型に変換 # 二次元配列化
x1_4 = np.array(x1_4, 'f').reshape(4,-1)
x1 = x1_4[:1]
# 重みの初期値をランダムに作成
W = np.random.randn(300,4)
x14_W = np.dot(x1_4, W)
x1 = np.dot(x1, W)

# ソフトマックス関数
x14_W = F.softmax(x14_W)
x1 = F.softmax(x1)

# 教師ラベル用意
label_data = pd.read_csv('data/y_train.txt', header=None)
y1_4 = label_data.iloc[0:4, :]
# int型に変換
y1_4 = np.array(y1_4, 'i')

y1 = y1_4[0]
y1_4 = y1_4.flatten()

# print(x14_W)
# print(y1_4)
# print(x1)
# print(y1)

# 目的関数を適用し、分類精度を計算
loss_1 = F.softmax_cross_entropy(x1, y1)
print(loss_1)

# print(x1)
# print(y1)
# print(x14_W)
# print(type(y1_4))

loss_1_4 = F.softmax_cross_entropy(x14_W, y1_4)
print(loss_1_4)
# accuracy_val = F.accuracy(y_val, t_val)
