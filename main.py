"""
Author: Jocer Franquiz
Date: 2022-12-23
Version: 1.0.0

This script orchestrate the whole process
"""


import subprocess
import yaml
import logging
import os

# Get the absolute path
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = os.path.join(ROOT_DIR, 'config.yml')


# Load the YAML file
with open(CONFIG_FILE, 'r') as f:
    config = yaml.safe_load(f)

# Set the variables from the config file
VIRTUAL_ENV = os.path.join(ROOT_DIR, config['VIRTUAL_ENV'], 'Scripts', 'activate_this.py')
LOG_FILE = os.path.join(ROOT_DIR, config['LOG_FILE'])
LOG_FORMAT = config['LOG_FORMAT']
LOG_LEVEL = config['LOG_LEVEL']

# Activate the virtual environment
with open(VIRTUAL_ENV, 'r') as f:
    exec(f.read(), {'__file__': VIRTUAL_ENV})

# Set up logging
logging.basicConfig(
    filename=LOG_FILE,
    level=LOG_LEVEL,
    format=LOG_FORMAT
)

scripts = [
    "extractor.py",
    "loader.py",
    "grid_plot.py",
    "process.py",
    "predictor.py",
]

for script in scripts:
    script_path = os.path.join(ROOT_DIR, script)
    python_path = os.path.join(ROOT_DIR, config['VIRTUAL_ENV'], 'Scripts', 'python.exe')
    try:
        logging.info(f"Running {script}. Path: {script_path}")
        subprocess.run([python_path, script_path], shell=True, check=True)
    except Exception as e:
        # Handle the error here
        logging.error(e)
