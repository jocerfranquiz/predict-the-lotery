import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import logging
import yaml

# Load the YAML file
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

# Set the variables from the config file
LOG_FILE = config['LOG_FILE']
LOG_FORMAT = config['LOG_FORMAT']
LOG_LEVEL = config['LOG_LEVEL']

# Set up logging
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=LOG_FORMAT)

# Load the CSV file into a DataFrame
try:
    df = pd.read_csv('tinka.csv', dtype={'id': np.int32, 'frequency': np.int32})
    logging.info("Data loaded successfully")
except FileNotFoundError as e:
    # Log the error
    logging.error(e)


df['id'] = df['id'] - 1
df['row'] = df['id'] // 6
df['col'] = df['id'] % 6

print(df.info())
print(df.head())

# Create a pivot grid of 8 rows and 6 columns
grid = df.pivot(index='row', columns='col', values='frequency')

# Fill the NaN values with 0
df_reshaped = grid.fillna(0)


# Get the values from the df_reshaped dataframe
data = df_reshaped.values

# Set up the plot
fig, ax = plt.subplots()

# Plot the heatmap
im = ax.imshow(data, cmap='coolwarm')

# Add axis labels
ax.set_xticks(range(data.shape[1]))
ax.set_yticks(range(data.shape[0]))

# Add tick labels
ax.set_xticklabels(range(1, data.shape[1] + 1))
ax.set_yticklabels(range(1, data.shape[0] + 1))

# Rotate the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add a colorbar
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('% probability', rotation=-90, va="bottom")

# Add the id numbers to each cell
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        id = i * data.shape[1] + j + 1
        ax.text(j, i, id, ha="center", va="center", color="w")

# Set the title and show the plot
plt.title('TINKA 945 2022_12')
plt.savefig('heatmap.png')

