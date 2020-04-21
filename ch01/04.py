sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.split()
i = 1
list = [1,5,6,7,8,9,15,16,19]
dic = {}
for word in words:
    if i in list:
        print(word[0])
        dic[word[0]] = i
    else:
        print(word[0:2])
        dic[word[0:2]] = i
    i += 1

print(dic)
