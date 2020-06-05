# ex61.py 単語の類似度Permalink
'''
“United States”と”U.S.”のコサイン類似度を計算せよ．
'''

from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
# binary :  If True, the data will be saved in binary word2vec format, else it will be saved in plain text.
print(model.similarity("United_States", "U.S."))
# print(model.wv.similarity("United_States", "U.S."))
