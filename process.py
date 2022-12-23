import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv('tinka.csv', dtype={'id': np.int32, 'frequency': np.int32})

# Set the index to the id column
# df.set_index('id', inplace=True)

print(df.describe())

df['frequency'].plot(
    kind='bar',
    figsize=(20, 10),
    title='Frequency of balls 2022',
    color=(30/256., 120/256., 180/256., 0.5),
    fontsize=8).set_xticklabels(df['id'], rotation=45)
plt.show()

# Calculate the probability of selecting each integer
df['probability'] = df['frequency'] / df['frequency'].sum()

# Set the number of samples
num_samples = 1000

# Initialize an empty list to store the results
sampling_results = []

# Loop over the number of samples
for i in range(num_samples):
    # Sample three integers without replacement using the probabilities
    sampled_ids = np.random.choice(df['id'], size=6, p=df['probability'])

    # Add the sampled integers to the results list
    sampling_results.append(sampled_ids)

# Convert the results list to a DataFrame
sampling_results_df = pd.DataFrame(sampling_results, columns=['b1', 'b2', 'b3', 'b4', 'b5', 'b6'])

# Save the results to a CSV file
sampling_results_df.to_csv('sim_data.csv', index=False)
