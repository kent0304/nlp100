# ex63.py 加法構成性によるアナロジーPermalink
'''
“Spain”の単語ベクトルから”Madrid”のベクトルを引き，”Athens”のベクトルを足したベクトルを計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ．
'''

from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
# binary :  If True, the data will be saved in binary word2vec format, else it will be saved in plain text.
result = model.most_similar(positive=["Spain", "Athens"], negative=["Madrid"])
for item in result:
    print(item)
