import logging
import requests
from bs4 import BeautifulSoup

TINKA_URL = "https://www.tinkaresultados.com/estadisticas"
LOG_FILE = "tinka.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.INFO
RAW_DATA_FILE = "raw_data.html"

# Set up logging
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=LOG_FORMAT)

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

