import chainer
import numpy as np
import pandas as pd
import chainer.links as L
import chainer.functions as F
from chainer import Variable

input_data = pd.read_csv('data/X_train.txt',sep=' ', header=None)
x1 = input_data.iloc[0, :]
x1_4 = input_data.iloc[0:5, :]

# float型に変換
x1 = np.array(x1, 'f').reshape(1,-1)
x1_4 = np.array(x1_4, 'f').reshape(4,-1)

# 重みの初期値をランダムに作成
W = np.random.randn(300,4)

x1_W = np.dot(x1, W)
x1_W = np.array(x1_W, 'f')

# print('1')
print(F.softmax(x1_W))

x14_W = np.dot(x1_4, W)
x14_W = np.array(x14_W, 'f')

# print('1-4')
print(F.softmax(x14_W))
