import pandas as pd
import numpy as np

# Create dataset
data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [20, np.nan, 22, 21, np.nan],
    'Marks': [85, 90, np.nan, 75, 88],
    'City': ['Chennai', 'Hyderabad', np.nan, 'Bangalore', 'Chennai']
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows containing missing values
df_cleaned = df.dropna()

print("\nDataset After Removing Missing Values:")
print(df_cleaned)
