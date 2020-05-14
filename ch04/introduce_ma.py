import MeCab


# パーサーの設定
# ChaSenという形態素解析器と互換の出力をする設定
me = MeCab.Tagger()
# 対象のテキスト
with open('neko.txt') as f:
    text = f.read()

result = me.parse(text)




file = "neko.txt.mecab"
fileobj = open(file, "w", encoding = "utf_8")
fileobj.write(result)
fileobj.close()
