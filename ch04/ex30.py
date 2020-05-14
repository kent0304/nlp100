import MeCab

# MeCabの出力フォーマット
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音

with open('neko.txt.mecab') as f:
    ma_list = f.readlines()

total_list =[]
for ma in ma_list:
    # 形態素一つごとにdictionary用意
    ma_dict = {}
    # \tで分割した最初の要素
    ma_dict['surface'] = ma.split('\t')[0]
    # \tで分割した後ろの要素をさらに','で分割

    # ma.split('\t')でうまく分けられないものもあるので条件分岐
    if len(ma.split('\t'))>=2:
        info = ma.split('\t')[1]
        ma_dict['base'] = info.split(',')[6]
        ma_dict['pos'] = info.split(',')[0]
        ma_dict['pos1'] = info.split(',')[1]
        # 形態素の情報をtotal_listに追加
        total_list.append(ma_dict)

print(total_list)
