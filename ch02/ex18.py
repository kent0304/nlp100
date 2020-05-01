### ex18.py
### 各行を3コラム目の数値の降順にソート

##--------pyhton------------
# readlinesはファイルの内容を読み出し1行ごとのリストにする
with open ('popular-names.txt') as f:
    contents = f.readlines()

# 3列目の要素だけのリスト
# ['Mary', 'Anna', ...]
elements = [content.split('\t')[2] for content in contents]


elements = [int(elm) for elm in elements]
newlst = sorted(elements, reverse=True)





##---------end--------------

##---------UNIX-------------
# わからない

##---------end--------------
