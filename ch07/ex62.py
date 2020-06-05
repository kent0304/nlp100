# ex62.py 類似度の高い単語10件Permalink
'''
“United States”とコサイン類似度が高い10語と，その類似度を出力せよ．
'''

from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
# binary :  If True, the data will be saved in binary word2vec format, else it will be saved in plain text.
ret = model.most_similar("United_States")
for item in ret:
    print(item)
