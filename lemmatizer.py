import string
import re

import spacy
from spacy.tokenizer import Tokenizer

from segmentator.helpers import *
import segmentator.constants as c


# This is for lemmatization
class Lemmatizer():
    def __init__(self, sentences=None):
        self.sentences = sentences

    def sentence_segmentation(self):
        # Load the spacy object
        nlp = spacy.load("en_core_web_sm")

        # List to hold the newly lemmatized sentences
        lemmatized_sentences = []
        for sent in self.sentences:
            print(f"\n {sent}")
            doc = nlp(sent)
            lemmatized_sentences.append([token.lemma_ for token in doc])
        return lemmatized_sentences

