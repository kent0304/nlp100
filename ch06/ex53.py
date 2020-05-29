# 53. 予測Permalink
'''
52で学習したロジスティック回帰モデルを用い，与えられた記事見出しからカテゴリとその予測確率を計算するプログラムを実装せよ．
'''

from sklearn.linear_model import LogisticRegression
import pandas as pd

train = pd.read_csv('train.feature.txt', index_col=0)

x_train = train.drop('CATEGORY', axis=1)
y_train = train['CATEGORY'].map({'b': 0, 't': 1, 'e': 2, 'm': 3})
# print(x_train)
lr = LogisticRegression(max_iter=1000)
lr.fit(x_train, y_train)

# 説明変数の係数
print("coefficient = ", lr.coef_)
# ロジスティック回帰モデルの切片
print("intercept = ", lr.intercept_)

# print(lr.predict_proba(x_train[0:4]))

def predict(x):
    out = lr.predict_proba(x)
    preds = out.argmax(axis=1)
    probs = out.max(axis=1)
    return preds, probs

preds, probs = predict(x_train)
print(pd.DataFrame([[y, p] for y, p in zip(preds, probs)], columns = ['予測', '確率']).head(5))
