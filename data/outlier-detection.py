import pandas as pd
import matplotlib.pyplot as plt

# Read in dataset 
df = pd.read_csv('data/formatted_data.csv')

# Select columns for processing outliers
#all_column = ['age', 'Mjob', 'Fjob', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']
all_column = df.columns.values()

# Give specific rows counts
for i in all_column:
    value_counts = df[i].value_counts().sort_index()
    print(value_counts)

# Draw bar chart for each column
for column in all_column:
    data_counts = df[column].value_counts().sort_index()
    plt.figure()
    data_counts.plot(kind='bar')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.title(f'Distribution of {column}')
    plt.show()
