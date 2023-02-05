# CLustering keywords - K-medoids and Edit distance

Project that clusters keywords based on Leventshtein algorithm and K-medoids method.

The script is using the streamlit library to easiest app deployment.

It is divided for 3 parts:
- **dataset** where users inputs their list of keywords, one keyword per line and chooseing the setting like the number of clusters and language. User choose the language of clustered keywords that are influence on the stopwords list downloaded from Spacy library.
- **model** - cleaning phrases from stopwords, creating matrix with distance metric and cluster keywords.
- **results** - writeing statistics about outliers and group of clustered keywords.

You can test the application under URL: https://nlp-project.streamlit.app/


