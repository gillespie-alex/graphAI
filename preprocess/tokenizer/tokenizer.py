import string
import re

import spacy
from spacy.tokenizer import Tokenizer

from tokenizer.helpers import *
import tokenizer.constants as c


'''
For my purposes this will not act like a regular tokenizer, as I use the Lemmatizer class for that,
I simply use this class to remove variuos stopwords and other custom words that wish to be removed
'''

class Tokenizer():
    def __init__(self, sentences=None):
        self.sentences = sentences

    def remove_words(self):
        res = []
        for sent in self.sentences:
            res.append(stopwords(sent))
        return res

