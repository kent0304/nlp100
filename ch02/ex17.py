### ex17.py
### １列目の文字列の異なり

##--------pyhton------------
string_list = []
with open ('col1.txt') as f:
    for line in f:
        elm = line.rstrip('\n')
        string_list.append(elm)

# 重複した要素を持たないset型を利用
print(set(string_list))



##---------end--------------

##---------UNIX-------------
# 並び替え
# sort col1.txt > col1_sort.txt
# uniqコマンドを適用する為には並び替えられている必要がある
# uniq col1_sort.txt

##---------end--------------
