# ex68.py Ward法によるクラスタリング
'''
国名に関する単語ベクトルに対し，Ward法による階層型クラスタリングを実行せよ．さらに，クラスタリング結果をデンドログラムとして可視化せよ．
'''
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

import pandas as pd
df = pd.read_csv('datasets_572274_1037156_wikipedia-iso-country-codes.csv')

print(df['English short name lower case'])



plt.figure(figsize=(32, 24))
link = linkage(vec, method='ward')
dendrogram(link, labels=countries)
plt.show()
