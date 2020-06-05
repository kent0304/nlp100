# ex67.py k-meansクラスタリング
'''
国名に関する単語ベクトルを抽出し，k-meansクラスタリングをクラスタ数k=5として実行せよ．
'''
# 既存のモデルダウンロード
from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
# binary :  If True, the data will be saved in binary word2vec format, else it will be saved in plain text.

import pandas as pd
df = pd.read_csv('datasets_572274_1037156_wikipedia-iso-country-codes.csv')

print(df['English short name lower case'])


from sklearn.cluster import KMeans
