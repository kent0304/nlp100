# ex60.py 単語ベクトルの読み込みと表示
'''
Google Newsデータセット（約1,000億単語）での学習済み単語ベクトル（300万単語・フレーズ，300次元）をダウンロードし，
”United States”の単語ベクトルを表示せよ．
ただし，”United States”は内部的には”United_States”と表現されていることに注意せよ．
'''
from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
# binary :  If True, the data will be saved in binary word2vec format, else it will be saved in plain text.
print(model["United_States"])
