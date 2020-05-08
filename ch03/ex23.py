# セクション構造Permalink
## 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

import jsonload
british_text = jsonload.british_text

import re

# 文字列リテラルの頭にrをつけると，エスケープシーケンスが無効
# findallは重複しない全てのマッチを文字列リストで表す
# british_textは複数行からなるので，re.MULTILINEを指定すると文字列の先頭と末尾にもアクセスできる
result = re.findall(r'^(.*==+.*==+.*)$', british_text, flags=re.MULTILINE)


# 各行において'==' が入っていればカウントしレベルを付与
for line in result:
    if '=====' in line:
        line = line.replace('=====', '')
        line += ' ' + '4'
    elif '====' in line:
        line = line.replace('====', '')
        line += ' ' + '3'
    elif '===' in line:
        line = line.replace('===', '')
        line += ' ' + '2'
    elif '==' in line:
        line = line.replace('==', '')
        line += ' ' + '1'
    print(line)
