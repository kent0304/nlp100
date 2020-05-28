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
