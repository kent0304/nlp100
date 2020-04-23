sequence = "I am an NLPer"

def ngram_maker(sequence, n):
    return [sequence[elm:elm+n] for elm in range(len(sequence) - n + 1)]

print(ngram_maker(sequence, 2))

words_sequence = sequence.split()

print(ngram_maker(words_sequence, 2))
