# 09
# Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文を与え，その実行結果を確認せよ．

import random

def Typoglycemia(sentence):
    words = sentence.split() # 文章を単語に分割しリストに格納
    new_sentence=[]
    for word in words:
        if len(word) <= 4: # 単語の文字数4以下の場合はそのまま
            new_word = word
        else:
            new_word = word[0] + ''.join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1]
            # 単語の先頭，末尾はそのまま．間はランダム関数で入れ替える
        new_sentence.append(new_word)
        # new_wordを新しいリストに格納

    return ' '.join(new_sentence)

print("Input:")
sentence = input()
# sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(Typoglycemia(sentence))
