### ex14.py
### 先頭からN行を出力

##--------pyhton------------
print("自然数Nは？：")
N = int(input())

with open ('popular-names.txt') as f:
    # 各行のインデックスと値をenmumerate
    for i,line in enumerate(f):
        # iがNに達した時点で終了
        if i >= N:
            break
        print(line.rstrip('\n'))


##---------end--------------

##---------UNIX-------------
# head -n 行数　ファイル名
# head -n 2  popular-names.txt

# sed -n '(開始行),(終了行)p' (ファイル名)
# cat popular-names.txt | sed -n '1,(Nの値)p'
##---------end--------------

# OK
