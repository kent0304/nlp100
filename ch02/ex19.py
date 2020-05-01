### ex19.py
### 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

##--------pyhton------------
from collections import Counter

# readlinesはファイルの内容を読み出し1行ごとのリストにする
with open ('popular-names.txt') as f:
    contents = f.readlines()

# 1列目の要素だけのリスト
# ['Mary', 'Anna', ...]
elements = [content.split('\t')[0] for content in contents]

newlst = sorted(elements, key=Counter(elements).get, reverse=True)
c = Counter(newlst)
print(c)



##---------end--------------

##---------UNIX-------------
# cut -f 1 popular-names.txt |sort| uniq -c|sort --reverse

##---------end--------------
# OK
