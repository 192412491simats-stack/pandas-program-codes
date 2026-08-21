import pandas as pd

# Create dataset
data = {
    'Name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'EEE', 'EEE'],
    'Marks': [85, 90, 78, 88, 75, 82]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Group data by Department
grouped = df.groupby('Department')['Marks'].mean()

print("\nAverage Marks by Department:")
print(grouped)
