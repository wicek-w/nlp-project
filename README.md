# CLustering keywords - K-means and Edit distance

Project that clusters keywords based on Leventshtein algorithm and K-means method.

The script is using the streamlit library to easiest app deployment.

It is divided for 3 parts:
- **user input** where users write their list of keywords, one keyword per line and chooseing the settings like the number of clusters and language. Language of clustered keywords influence on the stopwords list downloaded from Spacy library.
- **model** - cleaning phrases from stopwords, creating matrix with distance metric and cluster keywords using Kmeans method.
- **results** - writing group of keywords. The name of clustster is chosen by looking for the shortest keyword in the group.

You can test the application under URL: https://nlp-project.streamlit.app/ or by running `streamlit run streamit_app.py`.


