### ex16.py
### ファイルをN分割するPermalink

##--------pyhton------------
print("自然数Nは？：")
N = int(input())

# 行数カウント
count=0
with open ('popular-names.txt') as f:
    for line in f:
        count += 1

print(count)

with open ('popular-names.txt') as f:
    # 各行のインデックスと値をenmumerate
    for i,line in enumerate(f):
        # iが(全体-N)に達した時点で終了
        print(line.rstrip('\n'))
        if i == (count//N):
            print('\n')
        continue



##---------end--------------

##---------UNIX-------------


##---------end--------------
