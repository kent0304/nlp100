import jsonload
british_text = jsonload.british_text

import re


# 文字列リテラルの頭にrをつけると，エスケープシーケンスが無効
# findallは重複しない全てのマッチを文字列リストで表す
# british_textは複数行からなるので，re.MULTILINEを指定すると文字列の先頭と末尾にもアクセスできる
result = re.findall(r'^(.*\[\[Category:.*\]\].*)$', british_text, flags=re.MULTILINE)


# '[[Category:' と ']]' を除去
for line in result:
    content = line.replace('[[Category:', '').replace(']]', '')
    print(content)
