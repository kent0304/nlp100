# ex80 ID番号への変換
'''
問題51で構築した学習データ中の単語にユニークなID番号を付与したい．
学習データ中で最も頻出する単語に1，2番目に頻出する単語に2，……といった方法で，
学習データ中で2回以上出現する単語にID番号を付与せよ．
そして，与えられた単語列に対して，ID番号の列を返す関数を実装せよ．
ただし，出現頻度が2回未満の単語のID番号はすべて0とせよ
'''

import pandas as pd
import numpy as np
import re

# 1列目にカテゴリ、2列目に記事のタイトル（文章そのまま）
x_train = pd.read_csv('../ch08/data/train.txt', sep='\t', header=None)
# 記事タイトルのseries
x_train = x_train.iloc[:, 1]

# 辞書型で用意
dict = {}


for sentence in x_train:
    # 特殊表現は正規表現で除去
    sentence = re.sub('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]', ' ', sentence)
    for word in sentence.split():
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

# 並び替え
dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)

# 単語ID管理
dict = {word: i+1 for i, (word, cnt) in enumerate(dict) if cnt>1}


# 以下で確認
# for key in list(dict)[:10]:
#     print(f'{key}: {dict[key]}')

# 単語のIDを返す関数
def encode_word(word,dict):
    return dict[word]



# 文章のIDを返す関数
def encode_sentence(sentence,dict):
    new_sentence = []
    # 特殊表現は正規表現でスペースに変換
    sentence = re.sub('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]', ' ', sentence)
    for word in sentence.split():
        if word in dict:
            word = encode_word(word,dict)
        else:
            word = 0
        new_sentence.append(str(word))
    return ' '.join(new_sentence)

# 以下で確認
# sentence = "Home Depot Finally Bids Farewell to Fax Machines"
# print(encode_sentence(sentence, dict))
