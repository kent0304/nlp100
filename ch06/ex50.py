# 50. データの入手・整形
'''
News Aggregator Data Setをダウンロードし、以下の要領で学習データ（train.txt），検証データ（valid.txt），評価データ（test.txt）を作成せよ．

ダウンロードしたzipファイルを解凍し，readme.txtの説明を読む．
情報源（publisher）が”Reuters”, “Huffington Post”, “Businessweek”, “Contactmusic.com”, “Daily Mail”の事例（記事）のみを抽出する．
抽出された事例をランダムに並び替える．
抽出された事例の80%を学習データ，残りの10%ずつを検証データと評価データに分割し，それぞれtrain.txt，valid.txt，test.txtというファイル名で保存する．
ファイルには，１行に１事例を書き出すこととし，カテゴリ名と記事見出しのタブ区切り形式とせよ（このファイルは後に問題70で再利用する）．
学習データと評価データを作成したら，各カテゴリの事例数を確認せよ．
'''

import csv
import random
from sklearn.model_selection import train_test_split

# 引数delimiterに任意の文字列を区切り文字として指定(デフォルトはカンマ)
with open('../NewsAggregatorDataset/newsCorpora.csv') as f:
    reader = csv.reader(f, delimiter = '\t')
    dataset = [row for row in reader]

# publisherにより選別
new_dataset = [row for row in dataset if row[3]=='Reuters' or row[3]=='Huffington Post' or row[3]=='Businessweek' or row[3]=='Contactmusic.com' or row[3]=='“Daily Mail”']


with open('newsdata.txt', 'w') as f:
    writer = csv.writer(f, delimiter = '\t')
    writer.writerows(new_dataset)


train_data, valid__test_data = train_test_split(new_dataset, train_size=0.8, random_state=0)
valid_data, test_data = train_test_split(valid__test_data, test_size=0.5, random_state=0)

print('学習データ事例数:')
print(len(train_data))
print('検証データ事例数:')
print(len(valid_data))
print('試験データ事例数:')
print(len(test_data))

with open('train.txt', 'w') as f:
    writer = csv.writer(f, delimiter = '\t')
    writer.writerows(train_data)

with open('valid.txt', 'w') as f:
    writer = csv.writer(f, delimiter = '\t')
    writer.writerows(valid_data)

with open('test.txt', 'w') as f:
    writer = csv.writer(f, delimiter = '\t')
    writer.writerows(test_data)
