import chainer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
x, t = load_iris(return_X_y=True)
x = x.astype('float32')
t = t.astype('int32')

from chainer.datasets import TupleDataset
dataset = TupleDataset(x, t)

from chainer.datasets import split_dataset_random
train_val, test = split_dataset_random(dataset, int(len(dataset) * 0.7), seed=0)
train, valid = split_dataset_random(train_val, int(len(train_val) * 0.7), seed=0)


from chainer.iterators import SerialIterator

train_iter = SerialIterator(train, batch_size=4, repeat=True, shuffle=True)

minibatch = train_iter.next()

minibatch



import chainer
import chainer.links as L
import chainer.functions as F


class Net(chainer.Chain):

    def __init__(self, n_in=4, n_hidden=3, n_out=3):
        super().__init__()
        with self.init_scope():
            self.l1 = L.Linear(n_in, n_hidden)
            self.l2 = L.Linear(n_hidden, n_hidden)
            self.l3 = L.Linear(n_hidden, n_out)

    def forward(self, x):
        h = F.relu(self.l1(x))
        h = F.relu(self.l2(h))
        h = self.l3(h)

        return h

net = Net()
net = Net(n_hidden=100)

from chainer import optimizers
from chainer.optimizer_hooks import WeightDecay

optimizer = optimizers.SGD(lr=0.001)  # 学習率を 0.01 に設定
optimizer.setup(net)

for param in net.params():
    if param.name != 'b':  # バイアス以外だったら
        param.update_rule.add_hook(WeightDecay(0.0001))  # 重み減衰を適用

        from chainer import optimizers
from chainer.optimizer_hooks import WeightDecay

optimizer = optimizers.MomentumSGD(lr=0.001, momentum=0.9)
optimizer.setup(net)

for param in net.params():
    if param.name != 'b':  # バイアス以外だったら
        param.update_rule.add_hook(WeightDecay(0.0001))  # 重み減衰を適用

n_batch = 64  # バッチサイズ
n_epoch = 50  # エポック数

# ログ
results_train, results_valid = {}, {}
results_train['loss'], results_train['accuracy'] = [], []
results_valid['loss'], results_valid['accuracy'] = [], []

train_iter.reset()  # 上で一度 next() が呼ばれているため

count = 1

# ミニバッチの取得
train_batch = train_iter.next()

# x と t に分割
# データを GPU に転送するために、concat_examples に gpu_id を渡す
x_train, t_train = chainer.dataset.concat_examples(train_batch)

print(x_train)
print(type(t_train))
# 予測値と目的関数の計算
y_train = net(x_train)
print(y_train)
# loss_train = F.softmax_cross_entropy(y_train, t_train)
# acc_train = F.accuracy(y_train, t_train)
