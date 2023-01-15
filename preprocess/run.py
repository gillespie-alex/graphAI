# Import 3rd party libraries
import numpy as np

# Import standard python libraries
from collections import deque

# Import custom made packages
from segmentator import *
from lemmatizer import *
from tokenizer import *
# 2 lines between package imports and code


def load_text():
    with open("instructions.txt") as f:
        text = f.readlines()

    new_txt = [elem.strip('\n') for elem in text]
    return ' '.join(new_txt)

# Triggers the entire preprocess project
def run():
    new_txt = load_text()
    print('\n')
    print(new_txt)
    obj = Segmentator(new_txt)
    lists = obj.sentence_segmentation()
    print('\n')
    print(lists)
    obj2 = Lemmatizer(lists)
    lemma_sent = obj2.sentence_segmentation()
    print('\n')
    print(lemma_sent)
    obj3 = Tokenizer(lemma_sent)
    final = obj3.remove_words()
    print('\n')
    print(final)


if __name__ == '__main__':
    run()

