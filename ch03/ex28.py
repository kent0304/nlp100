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


# 強調マークアップの除去
markup_pattern = re.compile(r'\'{2}|\'{3}|\'{5}', flags=re.MULTILINE)
# 内部リンクの除去
link_pattern = re.compile(r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]', flags=re.MULTILINE)

# ex28.py 変更部分------------------------------------
# Template:Langの除去        {{lang|言語タグ|文字列}}
lang_pattern = re.compile(r'\{\{lang(?:[^|]*?\|)*?([^|]*?)\}\}', flags=re.MULTILINE)
# 外部リンクの除去  [http://xxxx] 、[http://xxx xxx]
# http_pattern = re.compile(r'\[http:\/\/(?:[^\s]*?\s)?([^]]*?)\]', flags=re.MULTILINE)

http_pattern = re.compile(r'''
        \[http:\/\/ # '[http://'（マークアップの開始）
        (?:         # キャプチャ対象外のグループ開始
            [^\s]*? # 空白以外の文字が0文字以上、非貪欲
            \s      # 空白
        )?          # グループ終了、このグループが0か1出現
        ([^]]*?)    # キャプチャ対象、']'以外が0文字以上、非貪欲（表示対象の文字列）
        \]          # ']'（マークアップの終了）
        ''', re.MULTILINE + re.VERBOSE)
# <br>、<ref>の除去
brref_pattern = re.compile(r'<\/?[br|ref][^>]*?>', flags=re.MULTILINE)

for line in new_result:
    tmp_makeup = markup_pattern.sub('', line[1])
    tmp_link = link_pattern.sub('', tmp_makeup)
    tmp_lang = lang_pattern.sub('', tmp_link)
    tmp_http = http_pattern.sub('' ,tmp_lang)
    tmp_brref = brref_pattern.sub('', tmp_http)

    dict[line[0]] = link_pattern.sub('', tmp_brref)

print(dict)


# ---------------------------------------------------
