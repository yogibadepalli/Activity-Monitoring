# data_loader.py
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """Loads data from the specified file path."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Cleans and preprocesses the dataset."""
    # Drop low-quality sensor readings and irrelevant columns
    columns_to_drop= ['hand_acceleration(±6g)_x','hand_acceleration(±6g)_y',  'hand_acceleration(±6g)_z','hand_orientation_1',  'hand_orientation_2','hand_orientation_3',  'hand_orientation_4',
                   'chest_acceleration(±6g)_x','chest_acceleration(±6g)_y',  'chest_acceleration(±6g)_z','chest_orientation_1',  'chest_orientation_2','chest_orientation_3',  'chest_orientation_4',
                    'ankle_acceleration(±6g)_x','ankle_acceleration(±6g)_y',  'ankle_acceleration(±6g)_z','ankle_orientation_1',  'ankle_orientation_2', 'ankle_orientation_3',  'ankle_orientation_4']  # Fill in the rest based on your file
    df.drop(columns=columns_to_drop, inplace=True)
    
    # Fill missing heart rate data using forward-fill
    df['heart_rate (bpm)'].fillna(method='ffill', inplace=True)
    
    # Drop rows with activity ID 0 (transient activities)
    df = df[df['activity ID'] != 0].reset_index(drop=True)
    
    return df

def split_data(df, target_column='activity ID', test_size=0.2):
    """Splits the dataset into training and testing sets."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=42)
