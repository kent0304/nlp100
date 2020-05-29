# 55. 混同行列の作成
'''
52で学習したロジスティック回帰モデルの混同行列（confusion matrix）を，学習データおよび評価データ上で作成せよ．
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

print('学習データ')
print('confusion matrix = \n', confusion_matrix(y_true=y_train, y_pred=lr.predict(x_train)))

print('評価データ')
print('confusion matrix = \n', confusion_matrix(y_true=y_test, y_pred=lr.predict(x_test)))
