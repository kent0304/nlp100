import myfunction

sequence1 = "paraparaparadise"
sequence2 = "paragraph"

X = myfunction.ngram_maker(sequence1,2)
Y = myfunction.ngram_maker(sequence2,2)

set_X = set(X)
set_Y = set(Y)

union = set_X | set_Y
print(union)

intersection = set_X & set_Y
print(intersection)

difference_X_Y = set_X - set_Y
difference_Y_X = set_Y - set_X
print(difference_X_Y)
print(difference_Y_X)

if 'se' in union:
    print("'se' is included")
else:
    print("'se' is not included")
