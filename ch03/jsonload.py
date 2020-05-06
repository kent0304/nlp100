import json

decoder = json.JSONDecoder()
res=[]

# rはreadのr．json読み込んで開く
with open('jawiki-country.json', 'r') as f:
    # readlineで1行毎に読み込む
    line = f.readline()
    while line:
        # raw_decodeはJSON文書をデコードし，pythonでの表現と文末のインデックスの2要素を返す
        res.append(decoder.raw_decode(line))
        line = f.readline()

for content in res:
    # 各contentは2つの要素が入ったtuple型
    if (content[0]['title']=='イギリス'):
        british_text = content[0]['text']
