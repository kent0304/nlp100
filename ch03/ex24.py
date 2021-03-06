# ファイル参照の抽出
## 記事から参照されているメディアファイルをすべて抜き出せ．
## [[ファイル:          |thumb|説明文]]

import jsonload
british_text = jsonload.british_text

import re

# 文字列リテラルの頭にrをつけると，エスケープシーケンスが無効
# findallは重複しない全てのマッチを文字列リストで表す
# ()で囲むことでキャプチャし，()で囲まれたものをそれぞれグループにして抽出できる
# (?:  )は()のキャプチャしないバージョン
result = re.findall(r'(?:ファイル):(.+?)\|', british_text)

for line in result:
    print(line)
