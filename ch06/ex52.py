# 52. 学習
'''
51で構築した学習データを用いて，ロジスティック回帰モデルを学習せよ．
'''

from sklearn.linear_model import LogisticRegression
import pandas as pd

train = pd.read_csv('train.feature.txt', index_col=0)

x_train = train.drop('CATEGORY', axis=1)
y_train = train['CATEGORY'].map({'b': 0, 't': 1, 'e': 2, 'm': 3})
# print(x_train)
lr = LogisticRegression(max_iter=1000)
print(lr.fit(x_train, y_train))
