# To model this data, we will use a combination of approaches.
# Use the text data collected along with the dates of the reports, geographic locations of the reports, and the shapes of the reported UAPs, and build a model to cluster the reports, considering them like points on a plane. The plane will have 3 dimensions: time, location (lat,long). The clusters will be the groups of reports that are similar to each other. This introduces another dimension to the plane: the shape of the UAPs. The clusters will be the groups of reports that are similar to each other after the text has been vectorized with TFIDF and the shape of the UAPs has been one-hot encoded.

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder

# import the dataset
data = pd.read_csv('./data/processed/nuforc_clean_plusfeatures.csv')

# one-hot encode the shape of the UAPs
enc = OneHotEncoder()
shape_encoded = enc.fit_transform(data[['shape']])

# vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer()
text_vectors = vectorizer.fit_transform(data['comments'])

# combine the encoded shape, text vectors, and location and time information
X = np.concatenate((shape_encoded.toarray(), text_vectors.toarray(), data[['latitude', 'longitude', 'year', 'month', 'day']].values), axis=1)

# perform k-means clustering
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
