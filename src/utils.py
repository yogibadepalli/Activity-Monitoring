# utils.py
import os

def get_data_path(filename):
    """Gets the full path to a data file."""
    return os.path.join(os.getcwd(), 'data', filename)
