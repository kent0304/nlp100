# 54. 正解率の計測Permalink
'''
52で学習したロジスティック回帰モデルの正解率を，学習データおよび評価データ上で計測せよ．
'''

from sklearn.linear_model import LogisticRegression
import pandas as pd

train = pd.read_csv('train.feature.txt', index_col=0)
x_train = train.drop('CATEGORY', axis=1)
y_train = train['CATEGORY'].map({'b': 0, 't': 1, 'e': 2, 'm': 3})

test = pd.read_csv('test.feature.txt', index_col=0)
x_test = test.drop('CATEGORY', axis=1)
y_test = test['CATEGORY'].map({'b': 0, 't': 1, 'e': 2, 'm': 3})


# print(test[0:10])

lr = LogisticRegression(max_iter=1000)
lr.fit(x_train, y_train)

# 説明変数の係数
# print("coefficient = ", lr.coef_)
# ロジスティック回帰モデルの切片
# print("intercept = ", lr.intercept_)

# print(lr.predict_proba(x_train[0:4]))

def predict(x):
    out = lr.predict_proba(x)
    preds = out.argmax(axis=1)
    probs = out.max(axis=1)
    return preds, probs

def accuracy(lr, xs, ts):
    ys = lr.predict(xs)
    return (ys == ts).mean()

print('訓練データ')
print(accuracy(lr, x_train, y_train))

print('試験データ')
print(accuracy(lr, x_test, y_test))
