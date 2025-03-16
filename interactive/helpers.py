import pandas as pd

DATA_DIR = '../data/dataset/'
DATA_SUFFIX = '_dataset.csv'

def load_data_as_df(file: str, data_dir = DATA_DIR, data_suffix = DATA_SUFFIX):
    return pd.read_csv(f'{data_dir}{file}{data_suffix}')

def check_missing_values(df: pd.DataFrame):
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]  # Filter to show only columns with missing values
    return missing_values

def time_based_train_test_split(df, date_column, test_size=0.2):
    """
    Split a DataFrame into train and test sets based on time.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to split
    date_column : str
        The name of the column containing date information
    test_size : float, default=0.2
        The proportion of the dataset to include in the test split
        
    Returns:
    --------
    X_train, X_test : pandas.DataFrame
        The train and test splits
    """
    # Ensure the date column is in datetime format
    if not pd.api.types.is_datetime64_any_dtype(df[date_column]):
        df[date_column] = pd.to_datetime(df[date_column])
    
    # Sort the DataFrame by date
    df_sorted = df.sort_values(by=date_column)
    
    # Calculate the split point
    split_idx = int(len(df_sorted) * (1 - test_size))
    
    # Split the data
    train_data = df_sorted.iloc[:split_idx]
    test_data = df_sorted.iloc[split_idx:]
    
    return train_data, test_data