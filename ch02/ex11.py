### ex11.py
### タブをスペースに置換

##--------pyhton------------

# 文字列としてlinesに代入
with open ('popular-names.txt') as f:
    lines = f.read()
# 置換
lines=lines.replace("\t", " ")

# 別ファイル名で保存
with open ('popular-names-without-tabs-python.txt', mode="w") as f:
    f.write(lines)

##---------end--------------

##---------UNIX-------------
# expand -t 2 (入力ファイル名) > (出力ファイル名)
##---------end--------------
