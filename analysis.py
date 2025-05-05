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

summary = iris.describe(include = 'all') # Include all columns
with open('iris_summary.txt', 'w') as f: # Open file in write mode
    f.write(str(summary)) # Write summary to file
print("Summary statistics saved to iris_summary.txt") # Print confirmation message

    


