import string
import re

import spacy
from spacy.tokenizer import Tokenizer

from segmentator.helpers import *
import segmentator.constants as c


# This is for word segmentation
class Segmentator():
    def __init__(self, corpus=None):
        self.corpus = corpus

    def sentence_segmentation(self):
        # Load the spacy object
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.corpus)
        assert doc.has_annotation("SENT_START")
        
        # Return a list of lists with each corresponding individual sentence
        sentences = [sent.text for sent in doc.sents if sent.text != '\n']
        return sentences

