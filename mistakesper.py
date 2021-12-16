def dice_coefficient(a, b):
    a_bigrams = set(a)
    b_bigrams = set(b)
    overlap = len(a_bigrams & b_bigrams)
    return int((overlap * 2.0/(len(a_bigrams) + len(b_bigrams)))*100)
