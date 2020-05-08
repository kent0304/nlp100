# テンプレートの抽出Permalink
## 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
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

for line in new_result:
    dict[line[0]] = line[1]

print(dict)
