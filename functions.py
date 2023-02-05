import streamlit as st
import numpy as np
from nltk.metrics.distance import edit_distance
from sklearn.cluster import KMeans
import advertools as adv
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer


def cleaning_data(keywords, lan = 'polish'):
    # we assume that user write clean keywords w\ interpunction
    stopwords = (list(adv.stopwords[lan]))
    for words in keywords:
        words = word_tokenize(words)
        words = [word for word in words if word not in stopwords]
        words = TreebankWordDetokenizer().detokenize(words)
    return keywords

def similarity(phrases):
    dist = np.array([[edit_distance(list(w1),list(w2)) for w1 in phrases] for w2 in phrases])
    dist = -1*dist
    return dist