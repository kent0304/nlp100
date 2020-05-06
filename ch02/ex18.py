### ex18.py
### 各行を3コラム目の数値の降順にソート

##--------pyhton------------
# readlinesはファイルの内容を読み出し1行ごとのリストにする
with open ('popular-names.txt') as f:
    contents = f.readlines()

contents.sort(key=lambda content: float(content.split('\t')[2]), reverse=True)


for content in contents:
    print(content, end='')




##---------end--------------

##---------UNIX-------------
# # 3カラム目を数値として逆順ソート
# sort hightemp.txt --key=3,3 --numeric-sort --reverse > result_test.txt
#
# # Pythonのプログラムで実行
# python main.py > result.txt
#
# # 結果の確認
# diff --report-identical-files result.txt result_test.txt

##---------end--------------
