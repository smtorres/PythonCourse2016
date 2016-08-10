
def has_no_e(word):
    """return true or false if there is no e in 'word'"""
    for letter in word:
        if letter=='e' or letter=='E': return False
    return True

def has_no_e(word):
    return not 'e' in word

def uses_only(word1,word2):
    """return true/false if word1 contains only letters from word2"""
    for letter in word1:
        if not letter in word2: return False
    return True

def uses_all(word1, word2):
    """return true/false if word1 uses all the letters in word2"""
    for letter in word2:
        if not letter in word1: return False
    return True

def uses_all(word1, word2):
    return uses_only(word2,word1)

def is_abecedarian(word):
    """is the word in alphabetical order?"""
    return [letter for letter in word] == sorted(word)

def is_abecedarian(word):
    """is the word in alphabetical order?"""
    return word == ''.join(sorted(word))

