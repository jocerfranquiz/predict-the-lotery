import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.cluster import DBSCAN


TEST_SIZE = 0.2
# Set the parameters for DBSCAN
EPS = 0.3622
MIN_SAMPLES = 13

# Load the data into a pandas dataframe
raw_data = pd.read_csv("sim_data.csv").to_numpy()

# Scale the data between 0 and 1
scaler = MinMaxScaler()
X = scaler.fit_transform(raw_data)

# Define the grid of possible values for eps and min_samples
param_grid = {"eps": np.linspace(0.1, 1, 10),
              "min_samples": np.arange(2, 10)}

# Create the model
model = DBSCAN()

# Split the data into training and testing sets
train_data, test_data = train_test_split(X, test_size=TEST_SIZE)
train_data = X

# Use DBSCAN to find clusters in the data
# Create the DBSCAN model
dbscan = DBSCAN(eps=EPS, min_samples=MIN_SAMPLES)

# Fit the model to the data
dbscan.fit(train_data)

# Get the labels for each point
labels = dbscan.labels_

# Get the number of clusters
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

# Get the number of outliers
n_outliers = list(labels).count(-1)

# Get the number of points in each cluster
cluster_sizes = [list(labels).count(i) for i in range(n_clusters)]

# Get centers of the clusters
centers = dbscan.components_

# Convert the centers to the original scale
centers = scaler.inverse_transform(centers)

print(f"Number of clusters: {n_clusters}")
print(f"Number of outliers: {n_outliers}")

# Print label, cluster size and center for each cluster
for i in range(n_clusters):
    print(f"Cluster {i}: {cluster_sizes[i]} points, center: {centers[i]}")


