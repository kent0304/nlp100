# ex65.py アナロジータスクでの正解率
'''
64の実行結果を用い，意味的アナロジー（semantic analogy）と文法的アナロジー（syntactic analogy）の正解率を測定せよ
'''

from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
# binary :  If True, the data will be saved in binary word2vec format, else it will be saved in plain text.

with open('new-questions-words.txt') as f:
    data = f.read().splitlines()

total_count = sum(data)
correct_count = 0
for row in data:
    row_list = row.split(' ')
    name = row_list[-2]
    similarity = row_list[-1]
    if row_list[-3] == row_list[-2]:
        correct_count += 1

accuracy = 100 * (correct_count / total_count)
print(accuracy)
