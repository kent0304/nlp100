# ex66.py WordSimilarity-353での評価Permalink
'''
The WordSimilarity-353 Test Collectionの評価データをダウンロードし，
単語ベクトルにより計算される類似度のランキングと，人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
'''
# 既存のモデルダウンロード
from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
# binary :  If True, the data will be saved in binary word2vec format, else it will be saved in plain text.

import pandas as pd
df = pd.read_csv('wordsim353/combined.csv')

# word2vecを用いた類似度を管理するリスト
word2vec_similarity = []

for i in range(len(df)):
    row = df.iloc[i]
    word2vec_similarity.append(model.similarity(line['Word 1'],line['Word 2']))

# 新しいカラム追加
df['w2v_sim'] = word2vec_similarity

# スピアマン相関係数
df[['Human (mean)', 'w2v_sim']].corr(method='spearman')
