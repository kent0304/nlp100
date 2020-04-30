### ex12.py
### 1列目をcol1.txtに，2列目をcol2.txtに保存

##--------pyhton------------

# それぞれの行の専用リストを用意
row1 = []
row2 = []
with open ('popular-names.txt') as f:
    # 各行を変数lineに代入
    for line in f:
        # splitで区切ったリストをstring_listに代入
        string_list=line.split()
        # string_listの1列目・2列目をappend
        row1.append(string_list[0])
        row2.append(string_list[1])

# 別ファイル名で保存
with open ('col1.txt', mode="w") as f:
    for line in row1:
        # 各行の値と改行を同時に書き込み
        f.write(line+"\n")

# 別ファイル名で保存
with open ('col2.txt', mode="w") as f:
    for line in row2:
        f.write(line+"\n")

##---------end--------------

##---------UNIX-------------
# -fオプションは区切られた項目の中で，表示したい項目を指定
# cut -f (項目数) (ファイル名)
# cut -f 1 popular-names.txt
# cut -f 2 popular-names.txt


# diffを取る
# diff --report-identical-files col1.txt col1_unix.txt
# diff --report-identical-files col2.txt col2_unix.txt
##---------end--------------
