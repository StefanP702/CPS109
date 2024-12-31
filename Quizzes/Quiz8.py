def has_dupilcate(text):
    for i in range(len(text)):
        if text[i] in text[i+1:]:
            return 1
    return 0