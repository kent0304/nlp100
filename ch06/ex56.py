# 56. 適合率，再現率，F1スコアの計測
'''
52で学習したロジスティック回帰モデルの適合率，再現率，F1スコアを，評価データ上で計測せよ．
カテゴリごとに適合率，再現率，F1スコアを求め，カテゴリごとの性能をマイクロ平均（micro-average）とマクロ平均（macro-average）で統合せよ．
'''

from sklearn.linear_model import LogisticRegression
import pandas as pd

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

train = pd.read_csv('train.feature.txt', index_col=0)
x_train = train.drop('CATEGORY', axis=1)
y_train = train['CATEGORY'].map({'b': 0, 't': 1, 'e': 2, 'm': 3})

test = pd.read_csv('test.feature.txt', index_col=0)
x_test = test.drop('CATEGORY', axis=1)
y_test = test['CATEGORY'].map({'b': 0, 't': 1, 'e': 2, 'm': 3})



lr = LogisticRegression(max_iter=1000)
lr.fit(x_train, y_train)

print('precision = ', precision_score(y_true=y_train, y_pred=lr.predict(x_train)))
print('recall = ', recall_score(y_true=y_train, y_pred=lr.predict(x_train)))
print('f1 score = ', f1_score(y_true=y_train, y_pred=lr.predict(x_train)))
