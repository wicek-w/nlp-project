import streamlit as st
import pandas as pd
from nltk.metrics.distance import edit_distance
import advertools as adv
from nltk import word_tokenize
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
import Pycluster as PC

# settings
nltk.download('punkt')

def cleaning_data(keywords, lan = 'polish'):
    # we assume that user write clean keywords w\ interpunction
    stopwords = (list(adv.stopwords[lan]))
    words = word_tokenize(keywords)
    words = [word for word in words if word not in stopwords]
    words = TreebankWordDetokenizer().detokenize(words)
    return words

header = st.container()
dataset = st.container()
model = st.container()
results = st.container()

with header:
    st.title("Clustering keywords")

with dataset:
    # input a keywords
    st.header("Please write your keywords")
    kw_input = pd.DataFrame(st.text_area("IMPORTANT! Each keyword should be in new line").split('\n'))
    kw_input = kw_input[0].tolist()
    st.write(kw_input)
    # language settings to choose stopwords list
    lan = st.selectbox("Choose the language", options=["polish", "english", "spanish"], index=0)
    nr_clusters = st.number_input(label='How many clusters?', min_value=2, key=2)

with model:
    keywords = cleaning_data(kw_input)

    # Edit distance - vector
    dist = [edit_distance(keywords[i], keywords[j])
            for i in range(1, len(keywords))
            for j in range(0,i)]

    labels, error, nfound = PC.kmedoids(dist, nclusters=nr_clusters)

    st.write("How many errors? {}" .format(len(error)))
    st.write("How many outliers? {}" .format(len(nfound)))

    st.write("You want to see the groups?")
    cluster = dict()

with results:
    # printing the results
    for word, label in zip(keywords, labels):
        cluster.setdefault(label, []).append(word)
    for label, grp in cluster.items():
        str.write(grp)



