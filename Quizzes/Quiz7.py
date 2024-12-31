def find_substring(word,substring): 
    for i in range(len(word)):
        if word[i:].startswith(substring):
            return i
    return -1