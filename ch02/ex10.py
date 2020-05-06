### ex10.py
### 行数のカウント


##--------pyhton------------
count = 0
# 該当ファイルをfとし，for文で１行ずつlineに代入
with open ('popular-names.txt') as f:
    for line in f:
        count += 1

print("行数：",count)
##---------end--------------

##---------UNIX-------------
# wcコマンドで以下を出力
# wc -l popular-names.txt
# 「（行数），（単語数），（ファイルサイズ）」
# それぞれ以下のオプションで指定が可能
# 「-l, -w, -c」
##---------end--------------
