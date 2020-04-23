import random

def Typoglycemia(sentence):
    words = sentence.split()
    new_sentence=[]
    for word in words:
        if len(word) <= 4:
            new_word = word
        else:
            new_word=""
            new_word += word[0] + ''.join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1]
        new_sentence.append(new_word)
    return ' '.join(new_sentence)

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(Typoglycemia(sentence))
