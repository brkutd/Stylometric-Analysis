import nltk
from nltk import punkt
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

LINES = ['-', ':', '--']


def text_to_string(filename):




def main():
    # create a dictionary with authors and their books converted into strings
    # 'unknown' is the object of study to assign it later to one of the two authors with stylometry
    strings_by_author = dict()
    strings_by_author['doyle'] = text_to_string('hound.txt')
    strings_by_author['wells'] = text_to_string('war.txt')
    strings_by_author['unknown'] = text_to_string('lost.txt')
    # test print
    print(strings_by_author['doyle'][:300])
    # form a dictionary with authors and their book converted into arrays of words
    words_by_author = make_word_dict(strings_by_author)
    # truncation - find the shortest corpus to cut the ends of the other two corpora
    len_shortest_corpus = find_shortest_corpus(words_by_author)

    word_length_test(words_by_author, len_shortest_corpus)
    stopwords_test(words_by_author, len_shortest_corpus)
    parts_of_speech_test(words_by_author, len_shortest_corpus)
    vocab_test(words_by_author)
    jaccard_test(words_by_author, len_shortest_corpus)


