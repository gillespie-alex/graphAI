import tokenizer.constants as c


# Holds all the helper functions for the tokenizer class
def stopwords(sentence):
    res = [word for word in sentence if word not in c.REMOVE_TOKENS]
    return res
