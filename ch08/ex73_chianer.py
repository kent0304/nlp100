# ex73.py 確率的勾配降下法による学習
'''
確率的勾配降下法（SGD: Stochastic Gradient Descent）を用いて，行列Wを学習せよ．
なお，学習は適当な基準で終了させればよい（例えば「100エポックで終了」など）．
'''
import chainer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 特徴量用意
x_train = pd.read_csv('data/X_train.txt',sep=' ', header=None)
x_valid = pd.read_csv('data/X_valid.txt',sep=' ', header=None)
x_test = pd.read_csv('data/X_test.txt',sep=' ', header=None)
# 教師ラベル用意
t_train = pd.read_csv('data/y_train.txt', header=None)
t_valid = pd.read_csv('data/y_valid.txt', header=None)
t_test = pd.read_csv('data/y_test.txt', header=None)

# float型に変換 # 二次元配列化
x_train = np.array(x_train, 'f')
x_valid = np.array(x_valid, 'f')
x_test = np.array(x_test, 'f')

# int型に変換
t_train = np.array(t_train, 'i')
t_valid = np.array(t_valid, 'i')
t_test = np.array(t_test, 'i')

# TupleDatasetを使って特徴量と教師ラベルをセットにする
from chainer.datasets import TupleDataset
train = TupleDataset(x_train,t_train)
valid = TupleDataset(x_valid,t_valid)
test = TupleDataset(x_test,t_test)

print(test)

# 用意したデータをどう抽出し，どうバッチわけするか設定する
from chainer import iterators
batchsize = 64
train_iter = iterators.SerialIterator(train, batchsize, shuffle=True, repeat=True)
valid_iter = iterators.SerialIterator(valid, batchsize, shuffle=True, repeat=True)
test_iter = iterators.SerialIterator(test, batchsize, shuffle=True, repeat=True)
# 何周も何周も全データを繰り返し読み出す必要がある場合はrepeat引数をTrue
# 1周が終わったらそれ以上データを取り出したくない場合はこれをFalse
# デフォルトではTrueなので本当は書かなくてもいい

# ------------------------------------------------------------------------------
# ネットワークの定義と最適化手法の選択
import chainer.links as L
import chainer.functions as F
# ネットワークの定義
class MLP(chainer.Chain):

    def __init__(self, n_mid_units=100, n_out=4):
        super().__init__()

        with self.init_scope():
            self.fc1 = L.Linear(None, n_mid_units)
            self.fc2 = L.Linear(n_mid_units, n_mid_units)
            self.fc3 = L.Linear(n_mid_units, n_out)

    def forward(self, x):
        h = F.relu(self.fc1(x))
        h = F.relu(self.fc2(h))
        h = self.fc3(h)
        return h

net = MLP() #インスタンス化

from chainer import optimizers
# 最適化手法の選択
optimizer = optimizers.SGD(lr=0.01)  # 学習率を 0.01 に設定
optimizer.setup(net)

# ------------------------------------------------------------------------------
# 学習における設定
# エポック数(↓変更可能)
n_epoch = 101

# 表示するログの設定
results_train, results_valid = {}, {}
results_train['loss'], results_train['accuracy'] = [], []
results_valid['loss'], results_valid['accuracy'] = [], []

count = 1

# train_batch = train_iter.next()
# x_train, t_train = chainer.dataset.concat_examples(train_batch)
# # print(t_train.flatten() )
# y_train = net(x_train)
# # print(y_train)
# loss_train = F.softmax_cross_entropy(y_train, t_train.flatten())
# print(loss_train)

# ------------------------------------------------------------------------------
# 実際の学習開始
for epoch in range(n_epoch):

    while True:
        # ミニバッチの取得
        train_batch = train_iter.next()

        # x と t に分割
        x_train, t_train = chainer.dataset.concat_examples(train_batch)

        # 予測値と目的関数の計算
        y_train = net(x_train)
        loss_train = F.softmax_cross_entropy(y_train, t_train.flatten())
        acc_train = F.accuracy(y_train, t_train.flatten())


        # 勾配の初期化と勾配の計算
        net.cleargrads()
        loss_train.backward()

        # パラメータの更新
        optimizer.update()

        # カウントアップ
        count += 1

        # 1エポック終えたら、valid データで評価する
        if train_iter.is_new_epoch:

            # 検証用データに対する結果の確認
            with chainer.using_config('train', False), chainer.using_config('enable_backprop', False):
                x_valid, t_valid = chainer.dataset.concat_examples(valid)
                y_valid = net(x_valid)
                loss_valid = F.softmax_cross_entropy(y_valid, t_valid.flatten())
                acc_valid = F.accuracy(y_valid, t_valid.flatten())

            # 結果の表示
            print('epoch: {}, iteration: {}, loss (train): {:.4f}, loss (valid): {:.4f}, acc (train): {:.4f}, loss (valid): {:.4f}'.format(epoch, count, loss_train.array.mean(), loss_valid.array.mean(), acc_train.array.mean(), acc_valid.array.mean()))

            # 可視化用に保存
            results_train['loss'].append(loss_train.array)
            results_valid['loss'].append(loss_valid.array)

            break
# ------------------------------------------------------------------------------
# 学習状況(誤差関数の遷移)の確認
# 目的関数(誤差関数，損失関数)の可視化
# 損失 (loss)
plt.plot(results_train['loss'], label='train')  # label で凡例の設定
plt.plot(results_valid['loss'], label='valid')  # label で凡例の設定
plt.title("Loss Function")
plt.xlabel("Epocks")
plt.ylabel("Loss")
plt.legend()  # 凡例の表示

plt.show()
