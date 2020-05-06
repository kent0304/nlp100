### ex16.py
### ファイルをN分割するPermalink
### トランプを分けるように交互に分割したほうがいい（データに偏りがあるので）

##--------pyhton------------
import math
print("自然数Nは？：")
N = int(input())

with open ('popular-names.txt') as f:
    lines = f.readlines();

count = len(lines)
unit = math.ceil(count/N) # 1ファイル当たりの行数

for i, offset in enumerate(range(0, count, unit), 1):
    with open ('child_{:02d}.txt'.format(i), mode="w") as out_file:
        for line in lines[offset:offset+unit]:
            out_file.write(line)




##---------end--------------

##---------UNIX-------------
# Nを入力
# echo -n "N--> "
# read n
#
# # 行数算出　wcは行数とファイル名を出力するのでcutで行数のみ切り出し
# count=`wc --line hightemp.txt | cut --fields=1 --delimiter=" "`
#
# # 1分割当たりの行数算出　余りがある場合は行数を+1
# unit=`expr $count / $n`
# remainder=`expr $count % $n`
# if [ $remainder -gt 0 ]; then
#     unit=`expr $unit + 1`
# fi
#
# # 分割
# split --lines=$unit --numeric-suffixes=1 --additional-suffix=.txt hightemp.txt child_test_
#
# # 検証
# for i in `seq 1 $n`
# do
#     fname=`printf child_%02d.txt $i`
#     fname_test=`printf child_test_%02d.txt $i`
#     diff --report-identical-files $fname $fname_test
# done

##---------end--------------
