### ex15.py
### 末尾のN行を出力

##--------pyhton------------
print("自然数Nは？：")
N = int(input())

# 行数カウント
count=0
with open ('popular-names.txt') as f:
    for line in f:
        count += 1

with open ('popular-names.txt') as f:
    # 各行のインデックスと値をenmumerate
    for i,line in enumerate(f):
        # iが(全体-N)に達した時点で終了
        if i >= (count-N):
            print(line.rstrip('\n'))
        continue



##---------end--------------

##---------UNIX-------------
# tail -n 行数 ファイル名
# tail -n 4  popular-names.txt

##---------end--------------

# OK
