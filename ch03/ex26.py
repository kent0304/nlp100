import jsonload
british_text = jsonload.british_text

import re

# 文字列リテラルの頭にrをつけると，エスケープシーケンスが無効
# findallは重複しない全てのマッチを文字列リストで表す
# ()で囲むことでキャプチャし，()で囲まれたものをそれぞれグループにして抽出できる
# re.DOTALLを足すと.に改行も対象となる
result = re.findall(r'^\{\{基礎情報.*?$(.*?)^\}\}$', british_text, flags=re.MULTILINE + re.DOTALL)
new_result = re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', result[0], flags=re.MULTILINE + re.DOTALL)

dict = {}

# ex26.py 変更部分------------------------------------
pattern = re.compile(r'\'{2}|\'{3}|\'{5}', flags=re.MULTILINE)

for line in new_result:
    dict[line[0]] = pattern.sub('', line[1])

print(dict)


# ---------------------------------------------------
