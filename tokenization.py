from spacy.tokenizer import Tokenizer
import re
import string
import spacy

def custom_tokenizer(nlp):

    special_cases = {"hello-world": [{"ORTH": "hello-world"}],
                     "subordinate": [{"ORTH": "sub"}, {"ORTH": "ordinate"}]}
    prefix_re = re.compile(r'''^[\[\("']''')
    suffix_re = re.compile(r'''[\]\)"']$''')
    infix_re = re.compile(r'''[-~]''')
    simple_url_re = re.compile(r'''^https?://''')

    return Tokenizer(nlp.vocab, rules=special_cases,
                                prefix_search=prefix_re.search,
                                suffix_search=suffix_re.search,
                                infix_finditer=infix_re.finditer,
                                url_match=simple_url_re.match)

def main():

    with open("instructions.txt") as f:
        text = f.readlines()

    new_txt = [elem.strip('\n') for elem in text]
    new_txt = ' '.join(new_txt)

    # Sentence Segmentation
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(new_txt)
    assert doc.has_annotation("SENT_START")
    sentences = [sent.text for sent in doc.sents if sent.text != '\n']
    print(sentences)

    # Lemmatizer
    #lem = nlp.get_pipe("lemmatizer")
    lemmatized_sentences = []
    for sent in sentences:
        doc = nlp(sent)
        lemmatized_sentences.append([token.lemma_ for token in doc])
    print(lemmatized_sentences)
    print('\n')
    #test_arr = ["box", "3.88", "\\", "faith", "\'"]
    remove_tokens = {
            '\'': True,
            '\\':True,
            '-': True,
            '.': True,
            ',': True,
            '\"': True,
            ' ': True,
            ')': True,
            '(': True,
            '{': True,
            '}': True,
            '[': True,
            ']': True,
            '!': True,
            '#': True,
            '@': True,
            '%': True,
            '$': True,
            '*': True,
            }


    print(remove_tokens)
    print('\n')
    #for elem in test_arr:
    #    if elem not in remove_tokens:
    #        print("not it")

    res = []
    for sent in lemmatized_sentences:
        res.append([word for word in sent if word not in remove_tokens])
    print(res)


if __name__ == '__main__':
    main()
