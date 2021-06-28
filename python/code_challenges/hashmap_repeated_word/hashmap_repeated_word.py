from code_challenges.hashtable.hashtable import Hashtable


def comb(string):
    words = string.replace(",", "").replace(".", "").split(" ")
    ht = Hashtable()
    for word in words:
        word = word.lower()
        if ht.contains(word):
            return word
        else:
            ht.add(key=word, value=word)
