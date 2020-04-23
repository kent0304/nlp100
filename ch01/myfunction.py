def ngram_maker(sequence, n):
    return [sequence[elm:elm+n] for elm in range(len(sequence) - n + 1)]
