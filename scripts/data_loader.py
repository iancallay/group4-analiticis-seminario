#%%
import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, '..', 'data', "US_0Superstore_data.xls")

def load_data(path):
    print(f"Loading data from {path}")
    
    try:
        data = pd.read_excel(path, sheet_name='Orders')
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    df = load_data(DATA_DIR)
    if df is not None:
        print(df.head())  # Display the first few rows of the dataframe
        df.info()  # Display summary information about the dataframe
    