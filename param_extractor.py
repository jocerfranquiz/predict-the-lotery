"""
Author: Jocer Franquiz
Date: 2022-12-23
Version: 1.0.0

This script helps to visually select eps and min_samples parameters for DBSCAN
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler

# Load the data into a pandas dataframe
raw_data = pd.read_csv("sim_data.csv").to_numpy()

# Scale the data between 0 and 1
scaler = MinMaxScaler()
X = scaler.fit_transform(raw_data)

# Create an array of eps values to try
eps_values = np.linspace(0.34, 0.4, 28)

# Create an array of min_samples values to try
min_samples_values = np.arange(7, 20)

param_data = pd.DataFrame(columns=["eps", "min_samples", "n_clusters", "n_outliers"])
loc = 0

# Loop through the values of eps
for eps in eps_values:

    for min_samples in min_samples_values:
        loc += 1
        # Create the DBSCAN model
        model = DBSCAN(eps=eps, min_samples=min_samples)

        # Fit the model to the data
        model.fit_predict(X)

        # Get the labels for each point
        labels = model.labels_

        # Get the number of clusters
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

        # Get the number of outliers
        n_outliers = list(labels).count(-1)

        # Add the results to the dataframe
        param_data.loc[loc] = [eps, min_samples, n_clusters, n_outliers]


# Plot the results
data_plot_o = param_data.pivot("eps", "min_samples", "n_outliers")
data_plot_c = param_data.pivot("eps", "min_samples", "n_clusters")

# Set up the plot with 2 subplots
fig, (axo, axc) = plt.subplots(1, 2)

# Plot the number of outliers
imo = axo.imshow(data_plot_o, cmap="coolwarm")
cbaro = axo.figure.colorbar(imo, ax=axo)
cbaro.ax.set_ylabel('Outliers', rotation=-90, va="bottom")
plt.xlabel("min_samples")
plt.ylabel("eps")
plt.xticks(np.arange(len(min_samples_values)), min_samples_values)
plt.yticks(np.arange(len(eps_values)), eps_values.round(4))

# Plot the number of clusters
imc = axc.imshow(data_plot_c, cmap="viridis")
cbarc = axc.figure.colorbar(imc, ax=axc)
cbarc.ax.set_ylabel('Clusters', rotation=-90, va="bottom")
plt.xlabel("min_samples")
plt.ylabel("eps")
plt.xticks(np.arange(len(min_samples_values)), min_samples_values)
plt.yticks(np.arange(len(eps_values)), eps_values.round(4))

plt.show()





"""

plt.figure(figsize=(6, 6))
# plt.contourf(param_data_plot, cmap="viridis")
# Plot side by side to compare
plt.subplot(1, 2, 1)

plt.imshow(param_data_plot, cmap="coolwarm")
plt.colorbar()
plt.xlabel("min_samples")
plt.ylabel("eps")
plt.xticks(np.arange(len(min_samples_values)), min_samples_values)
plt.yticks(np.arange(len(eps_values)), eps_values.round(4))
plt.show()

# TODO: add outliers to the plot
# I want the minimum of outliers with 5 clusters

"""

