import pandas as pd
import numpy as np
import gensim

# カンマ区切りでなくタブ区切りの時、sep="\t"を指定
train = pd.read_csv('data/train.txt', sep='\t', header=None)
valid = pd.read_csv('data/valid.txt', sep='\t', header=None)
test = pd.read_csv('data/test.txt', sep='\t', header=None)
model = gensim.models.KeyedVectors.load_word2vec_format('../ch07/GoogleNews-vectors-negative300.bin.gz', binary=True)

# 教師ラベル付与
dict = {'b':0, 't':1, 'e':2, 'm':3}
y_train = train.iloc[:,0].replace(dict)
y_train.to_csv('data/y_train.txt', header=False, index=False)
y_valid = valid.iloc[:, 0].replace(dict)
y_valid.to_csv('data/y_valid.txt', header=False, index=False)
y_test = test.iloc[:, 0].replace(dict)
y_test.to_csv('data/y_test.txt', header=False, index=False)

# 文章を単語ごとにベクトル化してその平均値を取り、これを特徴量とする。(n×300)
def set_X_vec(filename, df):
    with open(filename, "w") as f:
        for sentence in df.iloc[:,1]:
            # その文章を単語ごとにベクトル化して平均化したもの
            vectors = []
            for word in sentence.split():
                if word in model.vocab:
                    vectors.append(model[word])
            # もし一単語もベクトル化できなかったら0を配置
            if len(vectors)==0:
                vector = np.zeros(300)
            else:
                vectors = np.array(vectors)
                # 複数の単語ごとにベクトル化したリストの平均をとる
                vector = vectors.mean(axis=0)
            vector = vector.astype(np.str).tolist()
            output = ' '.join(vector) + '\n'
            f.write(output)

set_X_vec('data/X_train.txt', train)
set_X_vec('data/X_valid.txt', valid)
set_X_vec('data/X_test.txt', test)
