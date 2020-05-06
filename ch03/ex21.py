import jsonload
res = jsonload.res
# resの中身
# [
#   {{"title": "イギリス", "text": "イギリスという国は..."}, 68865}
#   {{"title": "ドイツ", "text": "ドイツという国は..."}, 103093}
#   {{"title": "フランス", "text": "フランスという国は..."}, 85398}
# ]

import re

for content in res:
    # 各contentは2つの要素が入ったtuple型
    if (content[0]['title']=='イギリス'):
        british_text = content[0]['text']


# 文字列リテラルの頭にrをつけると，エスケープシーケンスが無効
# findallは重複しない全てのマッチを文字列リストで表す
# british_textは複数行からなるので，re.MULTILINEを指定すると文字列の先頭と末尾にもアクセスできる
result = re.findall(r'^(.*\[\[Category:.*\]\].*)$', british_text, flags=re.MULTILINE)

for line in result:
    print(line)
