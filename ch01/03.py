sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = sentence.split()
count_list = []
for elm in list:
    count_list.append(len(elm) - elm.count(',') - elm.count('.'))
print(count_list)
