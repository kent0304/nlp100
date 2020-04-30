### ex13.py
### col1.txtとcol2.txtをマージ

##--------pyhton------------
# それぞれの行の専用リストを用意
row1 = []
row2 = []

with open ('col1.txt',"r") as f:
    # 各行を変数lineに代入
    for line in f:
        # 各行row1にappendする際，改行除去
        row1.append(line.rstrip('\n'))


with open ('col2.txt',"r") as f:
    # 各行を変数lineに代入
    for line in f:
        row2.append(line.rstrip('\n'))

# 別ファイル名で保存
with open ('merge.txt', mode="w") as f:
    # row1とrow2それぞれの要素を順番にzipで取得
    for elm1, elm2 in zip(row1, row2):
        f.write(elm1+" "+elm2+'\n')



##---------end--------------

##---------UNIX-------------
# dオプションで結合文字指定
# paste -d " "col1.txt col2.txt > merge_unix.txt

# diffを取る
# diff --report-identical-files merge.txt merge_unix.txt
##---------end--------------
