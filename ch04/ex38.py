import MeCab
import collections
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

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

# -------- ここからex38 ------------------
# 登場する形態素全て格納するリスト
ma_list=[]
for ma_dict in total_list:
    ma_list.append(ma_dict['surface'])

c = collections.Counter(ma_list)

# (要素, 出現回数)という形のタプルを出現回数順に並べたリスト c.most_common()
count_list = c.most_common()

# x = []
# count = []
#
# i = 0
# for tupple in count_list:
#     if i > 15:
#         break
#     x.append(tupple[0])
#     i += 1
#     # count.append(tupple[1])
#
# print(x)




plt.hist(count_list[:15], bins=10)
plt.title("ヒストグラム")
plt.xlabel("word")
plt.ylabel("count")
plt.show()
