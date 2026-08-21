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

# Fill numerical missing values with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Fill categorical missing values with mode
df['City'] = df['City'].fillna(df['City'].mode()[0])

print("\nDataset After Handling Missing Values:")
print(df)
