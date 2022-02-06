import nltk
from nltk import punkt
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

LINES = ['-', ':', '--']


def main():
    authors_with_strings = dict()
    authors_with_strings['doyle'] = text_to_string('hound.txt')
    authors_with_strings['wells'] = text_to_string('war.txt')
    authors_with_strings['unknown'] = text_to_string('lost.txt')
