# ex64.py アナロジーデータでの実験
'''
単語アナロジーの評価データをダウンロードし，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．求めた単語と類似度は，各事例の末尾に追記せよ
'''

from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
# binary :  If True, the data will be saved in binary word2vec format, else it will be saved in plain text.

with open('questions-words.txt') as f:
    data = f.read().splitlines()

# 上記のデータの最後にカラムを追加予定の新しいデータ
new_data = []
for row in data:
    if ':' in row:
        new_data.append(row)
        continue
    row_list = row.split(' ')
    # 類似度計算
    result = model.most_similar(positive = [row_list[1], row_list[2]], negative = [row_list[0]], topn = 1)
    # print(result)
    row = row + ' ' + " ".join(map(str, result))
    new_data.append(row)

with open('new-questions-words.txt', mode="w") as f:
    f.write('\n'.join(new_data))
