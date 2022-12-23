"""
Author: Jocer Franquiz
Date: 2022-12-23
Version: 1.0.0

This script cleans the html tables and translate it into CSV
"""


import pandas as pd

# Read the HTML table from the file into a list of DataFrames
df_list = pd.read_html('raw_data.html')

# Concatenate the DataFrames in the list
df = pd.concat(df_list[2:])

# Drop the middle column
df.drop(df.columns[1], axis=1, inplace=True)

# Change the column names "Bolilla" to ball and "Veces" to frequency
df.columns = ['id', 'frequency']


df.set_index('id', inplace=True)

for _ in range(1, 47):
    if _ not in df.index:
        df.loc[_] = 0

# Save the DataFrame as a CSV file
df.to_csv('tinka.csv')
