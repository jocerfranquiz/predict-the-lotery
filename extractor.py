"""
Author: Jocer Franquiz
Date: 2022-12-23
Version: 1.0.0

This script scrapps the data from the website
"""


import requests
from bs4 import BeautifulSoup

import os
import yaml
import logging

# Get the absolute path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = os.path.join(ROOT_DIR, 'config.yml')

# Load the YAML file
with open(CONFIG_FILE, 'r') as f:
    config = yaml.safe_load(f)
    
LOG_FILE = os.path.join(ROOT_DIR, config['LOG_FILE'])
LOG_FORMAT = config['LOG_FORMAT']
LOG_LEVEL = config['LOG_LEVEL']

# Set up logging
logging.basicConfig(
    filename=LOG_FILE,
    level=LOG_LEVEL,
    format=LOG_FORMAT
)

TINKA_URL = "https://www.tinkaresultados.com/estadisticas"
RAW_DATA_FILE = "raw_data.html"

# Define the response variable with a default value of None
response = None

try:
    # Send an HTTP GET request to the website
    response = requests.get(TINKA_URL)

    # Check if the request was successful
    if response.status_code == 200:
        # Log the response status code
        logging.info("Response status code: %s", response.status_code)

        # Parse the HTML response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the tables in the HTML response
        tables = soup.find_all('table')

except ConnectionError as e:
    # Log an error message if the request fails
    logging.error(f'Connection error: {e}')

except requests.exceptions.RequestException as e:
    # Log the error
    logging.error(e)
finally:
    # Close the HTTP connection
    response.close()

# Save the table as a text file
with open(RAW_DATA_FILE, 'w') as f:
    for table in tables:
        # Format the table as HTML
        f.write(table.prettify())

