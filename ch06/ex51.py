# 51. 特徴量抽出
'''
学習データ，検証データ，評価データから特徴量を抽出し，それぞれtrain.feature.txt，valid.feature.txt，test.feature.txtというファイル名で保存せよ．
 なお，カテゴリ分類に有用そうな特徴量は各自で自由に設計せよ．記事の見出しを単語列に変換したものが最低限のベースラインとなるであろう．
'''

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


# 元データ読み込み タブ区切りの時はread_table カンマ区切りならread_csv
train = pd.read_table('train.txt', names=['ID','TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])
valid = pd.read_table('valid.txt', names=['ID','TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])
test = pd.read_table('test.txt', names=['ID','TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])


# TdidfVectorizer()
vec_tfidf = TfidfVectorizer()

# ベクトル化
X_train = vec_tfidf.fit_transform(train['TITLE'])
X_valid = vec_tfidf.fit_transform(train['TITLE'])
X_test = vec_tfidf.fit_transform(train['TITLE'])

# print('Vocabulary size: {}'.format(len(vec_tfidf.vocabulary_)))
# print('Vocabulary content: {}'.format(vec_tfidf.vocabulary_))

# 特徴量のテーブル作成
trainf = pd.DataFrame(X_train.toarray(), columns=vec_tfidf.get_feature_names())
validf = pd.DataFrame(X_valid.toarray(), columns=vec_tfidf.get_feature_names())
testf = pd.DataFrame(X_test.toarray(), columns=vec_tfidf.get_feature_names())

# カテゴリのラベルカラム追加
train_feature = pd.concat([train['CATEGORY'], trainf], axis=1)
valid_feature = pd.concat([valid['CATEGORY'], validf], axis=1)
test_feature = pd.concat([test['CATEGORY'], testf], axis=1)

# 書き出し
train_feature.to_csv('train.feature.txt')
valid_feature.to_csv('valid.feature.txt')
test_feature.to_csv('test.feature.txt')
