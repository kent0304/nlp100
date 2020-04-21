string1 = "パトカー"
string2 = "タクシー"
length = len(string1)
new_string = ""
for i in range(length):
    new_string += string1[i] + string2[i]

print(new_string)
