# Commentary

these reports are scattered across multiple theoretical planes. We have longitude and latitude but we also have time. I want to find clusters in this 3d space. locations in the 2d plane where reports used similar words to describe what they saw.

One approach to finding clusters in this 3D space might be to use a density-based clustering algorithm such as DBSCAN. This algorithm works by identifying clusters as areas of high density separated by areas of low density.

To use DBSCAN, you will need to first determine a suitable distance measure between points in your 3D space. This could be Euclidean distance, for example, which takes into account the differences in longitude, latitude, and time. You will also need to choose a value for the DBSCAN eps parameter, which controls the size of the neighborhood around each point that is used to determine whether it is a core point (i.e., a point with sufficient neighbors to be considered part of a cluster).

Once you have these values, you can apply DBSCAN to your data to identify clusters of reports with similar words. You could then visualize the clusters in a 3D scatter plot to see the distribution of reports in this space.

Alternatively, you could consider using a different clustering algorithm such as k-means, which works by partitioning the data into a predefined number of clusters based on the mean of the points in each cluster. This approach might be more suitable if you have a specific number of clusters in mind, or if you want to use a more traditional clustering method.

Regardless of which approach you choose, it will likely be helpful to represent the reports in a numerical form, such as by using word embeddings or term frequency-inverse document frequency (TF-IDF) vectors, before applying a clustering algorithm. This will allow you to apply mathematical operations to the data and make it more amenable to analysis. But for analyzing "shape" or color, you may need to use a different approach.

One approach you could try is to use a named entity recognition (NER) model to extract the shapes mentioned in the reports and then use a clustering algorithm, such as DBSCAN, to identify clusters of reports that mention similar shapes. You could represent each report as a vector where each dimension corresponds to a particular shape, and the value at that dimension indicates the number of times that shape was mentioned in the report. Then you can apply DBSCAN using a distance measure such as Euclidean distance to find clusters of reports that mention similar shapes.

Alternatively, you could try using a natural language processing (NLP) technique such as Latent Semantic Analysis (LSA) or Latent Dirichlet Allocation (LDA) to extract topics from the reports and then use a clustering algorithm to identify clusters of reports that contain similar topics. This approach may be more effective at identifying patterns in the language used in the reports, rather than just the specific shapes mentioned.

# the elements to consider are:

- the shape of the UFO
- the color of the UFO
- the size of the UFO
- the speed of the UFO
- the direction of the UFO
- the altitude of the UFO
- the duration of the UFO
- the number of UFOs

# Response:
It sounds like you want to cluster the UFO sightings based on their descriptions. One approach you could take is to use a vector space model to represent each UFO sighting as a vector of the features you've listed. Then, you could apply a clustering algorithm such as DBSCAN to group the sightings into clusters based on the similarity of their feature vectors.

To determine a suitable distance measure for DBSCAN, you will need to consider the relative importance of each feature in your vector space. For example, if the shape of the UFO is more important than the color, you may want to weight the shape feature more heavily when calculating the distance between two sightings. One way to do this is to normalize the values of each feature to have a mean of 0 and a standard deviation of 1, and then apply different weights to each feature.

Alternatively, you could use a different distance measure such as cosine similarity, which takes into account the angle between two vectors rather than the Euclidean distance. This may be more appropriate if the magnitude of the feature values is not as important as the direction they point in.

As for choosing the value for the DBSCAN eps parameter, this will depend on the density of your data and the desired size of the clusters. A larger value for eps will result in more permissive clusters, while a smaller value will result in more strict clusters. You may need to experiment with different values to find one that gives you the desired results.

# Determining a distance measure for the Reports

We need to determine a distance measure between points in our 3D space. One option is to use Euclidean distance, which takes into account the differences in the 3 dimensions (longitude, latitude, and time). We can use the sklearn.metrics.pairwise_distances function to calculate the distance between each pair of points in our data. This function takes a matrix of data points as input and returns a matrix of distances between each pair of points. We can then use the scipy.spatial.distance.squareform function to convert this matrix into a condensed distance matrix, which is a 1D array of distances between each pair of points. This condensed distance matrix can then be used as input to the DBSCAN algorithm.

We can also use the scipy.spatial.distance.pdist function to calculate the condensed distance matrix directly. This function takes a matrix of data points as input and returns a condensed distance matrix of distances between each pair of points. We can then use the scipy.spatial.distance.squareform function to convert this condensed distance matrix into a square distance matrix, which is a 2D array of distances between each pair of points. This square distance matrix can then be used as input to the DBSCAN algorithm.

# Choosing the value for the DBSCAN eps parameter

We need to choose a value for the DBSCAN eps parameter, which controls the size of the neighborhood around each point that is used to determine whether it is a core point (i.e., a point with sufficient neighbors to be considered part of a cluster).

The value of eps should be chosen based on the distance measure being used and the characteristics of the data. For example, if we are using Euclidean distance and the data points are densely packed, we may want to choose a smaller value for eps. On the other hand, if the data points are more spread out, we may want to choose a larger value for eps.

To choose a value for eps, we can plot the distance between each pair of points in our data and look for an "elbow" in the plot. This elbow represents the point where the distances between points start to increase more rapidly, which suggests that points beyond this point are not part of the same cluster. We can then choose a value for eps slightly smaller than the distance at the elbow as the threshold for determining whether a point is a core point.

We can use the sklearn.neighbors.NearestNeighbors function to calculate the distance to the kth nearest neighbor for each point in our data. This function takes a matrix of data points as input and returns a matrix of distances to the kth nearest neighbor for each point. We can then use the scipy.spatial.distance.squareform function to convert this matrix into a condensed distance matrix, which is a 1D array of distances to the kth nearest neighbor for each point. This condensed distance matrix can then be used to plot a histogram of the distances to the kth nearest neighbor for each point.


We can use the sklearn.cluster.DBSCAN function to cluster the data points based on the distance measure and eps value we have chosen. This function takes the condensed distance matrix (or square distance matrix) and the eps value as input and returns a list of cluster labels for each point in the data. Points that are not part of any cluster will be given the label -1.

We can use the sklearn.metrics.silhouette_score function to calculate the silhouette score for the clusters. This function takes the condensed distance matrix (or square distance matrix) and the list of cluster labels as input and returns the silhouette score for the clusters.

The silhouette score is a measure of how well the clusters are separated from each other and how well they contain their own points. The silhouette score ranges from -1 to 1, where a score close to 1 indicates well-separated clusters and a score close to -1 indicates overlapping clusters.

We can use the sklearn.metrics.calinski_harabasz_score function to calculate the Calinski-Harabasz score for the clusters. This function takes the condensed distance matrix (or square distance matrix) and the list of cluster labels as input and returns the Calinski-Harabasz score for the clusters.

The Calinski-Harabasz score is a measure of how well the clusters are separated from each other and how well they contain their own points. The Calinski-Harabasz score ranges from 0 to infinity, where a score close to infinity indicates well-separated clusters.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import pdist, squareform

# Read in the data
df = pd.read_csv("../data/processed/ufos_processed.csv", low_memory=False, on_bad_lines= 'skip')

# Convert the latitude and longitude to radians
df['latitude_rad'] = np.radians(df['latitude'])
df['longitude_rad'] = np.radians(df['longitude'])

# Convert the latitude and longitude to cartesian coordinates
df['x'] = np.cos(df['latitude_rad']) * np.cos(df['longitude_rad'])
df['y'] = np.cos(df['latitude_rad']) * np.sin(df['longitude_rad'])
df['z'] = np.sin(df['latitude_rad'])

# Create a matrix of the x, y, and z coordinates
X = df[['x', 'y', 'z']].values

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Calculate the condensed distance matrix
distances = pdist(X_scaled)

# Calculate the distance to the kth nearest neighbor
k = 2
neigh = NearestNeighbors(n_neighbors=k)
nbrs = neigh.fit(X_scaled)
distances_k, indices_k = nbrs.kneighbors(X_scaled)
distances_k = distances_k[:, k-1]

# Plot a histogram of the distances to the kth nearest neighbor
plt.hist(distances_k, bins=50)
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.show()

# Choose a value for eps
eps = 0.5

# Run the DBSCAN algorithm
db = DBSCAN(eps=eps, min_samples=2, metric='precomputed')
db.fit(squareform(distances))

# Calculate the silhouette score
score = silhouette_score(squareform(distances), db.labels_)

# Calculate the Calinski-Harabasz score
score = calinski_harabasz_score(squareform(distances), db.labels_)

# Print the cluster labels
print(db.labels_)
```



# Step 5 - Running the DBSCAN algorithm

Run the DBSCAN algorithm on the preprocessed data, using the distance measure and eps value that you selected. This will generate clusters of points that are considered to be "similar" based on the distance measure and eps value. The DBSCAN algorithm will assign a cluster label to each point in the data, where points that are not part of any cluster will be given the label -1. The DBSCAN algorithm will also assign each point to either a core point or a border point, where core points are points with sufficient neighbors to be considered part of a cluster and border points are points that are not core points but are neighbors of a core point. The DBSCAN algorithm will also assign each point to either a noise point or a non-noise point, where noise points are points that are not part of any cluster and non-noise points are points that are part of a cluster. The DBSCAN algorithm will also assign each point to either a direct core point or an indirect core point, where direct core points are points that are core points and indirect core points are points that are not core points but are neighbors of a core point.



# Step 6 - Evaluating the results

Evaluate the results of the DBSCAN algorithm by calculating the silhouette score and Calinski-Harabasz score for the clusters. These scores will give you an idea of how well the clusters are separated from each other and how well they contain their own points. The silhouette score ranges from -1 to 1, where a score close to 1 indicates well-separated clusters and a score close to -1 indicates overlapping clusters. The Calinski-Harabasz score ranges from 0 to infinity, where a score close to infinity indicates well-separated clusters.