# analysis.py
# Iris Dataset Analysis

# Author: Marcin Kaminski
"""
This program will:
1. Output a summary of each variable to a single text file, 
2. Save a histogram of each variable to png files, and
3. Output a scatter plot of each pair of variables.
4. Perform any other analysis appropriate.
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
iris = pd.read_csv('iris.csv') # Load the dataset from CSV file

# Display the first 5 rows of the dataset
print(iris.head()) 

# 1. Output a summary of each variable to a single text file

summary = iris.drop(columns=['class']).describe() # Drop the 'class' column and get summary statistics
with open('iris_summary.txt', 'w') as f: # Open file in write mode
    f.write(str(summary)) # Write summary to file
print("Summary statistics saved to iris_summary.txt") # Print confirmation message

# 2. Save a histogram of each variable to png files

for column in iris.columns: # Loop through each column
    if column == 'class':
        continue # Skip the 'class' column
    plt.figure(figsize = (8, 6)) # Create a new figure with specified size
    sns.histplot(iris[column], kde=True) # Plot histogram with kernel density estimate
    plt.title(f'Histogram of {column}') # Set title
    plt.xlabel(column) # Set x axis label
    plt.ylabel('Frequency') # Set y axis label
    plt.grid(True) # Show grid
    plt.tight_layout() # Adjust layout to avoid label cutoff
    plt.savefig(f'{column}_histogram.png') # Save figure to file
    plt.close() # Close the figure
    print(f"Saved histogram: {column}_histogram.png") # Print confirmation message

# 3. Output a scatter plot of each pair of variables
    
numeric_columns = iris.select_dtypes(include=['float64', 'int64']).columns # Select numeric columns
for i, col1 in enumerate(numeric_columns): # Loop through each numeric column
    for col2 in numeric_columns[i+1:]: # Loop through each subsequent numeric column
        plt.figure(figsize=(8, 6)) # Create a new figure with specified size
        sns.scatterplot(data = iris, x = col1, y = col2, hue='class') # Create scatter plot with hue based on 'class'
        plt.title(f'Scatter plot of {col1} vs {col2}') # Set title
        plt.xlabel(col1) # Set x axis label
        plt.ylabel(col2) # Set y axis label
        plt.grid(True) # Show grid
        plt.tight_layout() # Adjust layout to avoid label cutoff
        plt.savefig(f'{col1}_{col2}_scatter_plot.png') # Save figure to file
        plt.close() # Close the figure
        print(f"Saved scatter plot: {col1}_{col2}_scatter_plot.png") # Print confirmation message


