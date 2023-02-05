import streamlit as st
import numpy as np
import pandas as pd
from nltk.metrics.distance import edit_distance
from sklearn.cluster import KMeans
import nltk
import functions as f
from sklearn.cluster import AffinityPropagation

# settings
nltk.download('punkt')
corpus_sentences_list =[]
cluster_name_list = []

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
    if st.button('Zaczynajmy!'):
        keywords = f.cleaning_data(kw_input, lan)

        distance = f.similarity(keywords)

        clusterer = KMeans(n_clusters=nr_clusters)
        clusterer.fit(distance)
        cluster_assignment = clusterer.labels_

        clustered_sentences = [[] for i in range(nr_clusters)]
        for sentence_id, cluster_id in enumerate(cluster_assignment):
            clustered_sentences[cluster_id].append(keywords[sentence_id])

        for nr, cluster in enumerate(clustered_sentences):
            for kw in cluster[:]:
                cluster_name_list.append("Grupa {}, #{} Elementów ".format(nr + 1, len(cluster)))
                corpus_sentences_list.append(kw)

        results = pd.DataFrame(sorted(zip(cluster_name_list,cluster_name_list, corpus_sentences_list)), columns=["cluster_id", "cluster_name", "keyword"])

        results["length"] = results["keyword"].astype(str).map(len)
        results = results .sort_values(by="length", ascending=True)

        results['cluster_name'] = results.groupby('cluster_name')['keyword'].transform('first')
        results.sort_values(['cluster_name', "keyword"], ascending=[True, True], inplace=True)

        results['cluster_name'] = results['cluster_name'].fillna("ups! nie przypisano do żadnego klastra")

        del results['length']
        st.table(results)




