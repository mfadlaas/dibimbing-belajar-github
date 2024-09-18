import pandas as pd

def read_csv(file_path):
    """Function to read a CSV file and return a DataFrame."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading the CSV file: {e}")