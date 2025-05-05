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
import pandas as pd # For data manipulation
import matplotlib.pyplot as plt # For plotting
import seaborn as sns # For advanced plotting
import json # For JSON handling
import subprocess # For running shell commands


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

# 4. Perform any other analysis appropriate
        
print('For additional analysis please refer to the Jupyter notebook analysis.ipynb') # Print message for additional analysis



""" The following code has been developed using ChatGPT (GPT-4o) from OpenAI.
----------------------------------------------------------------------------------------------------------------------------"""

# The below code is used to extract the contents of the Jupyter notebook analysis.ipynb

# Load the notebook JSON
with open('analysis.ipynb', 'r', encoding='utf-8') as f: # Open the notebook file in read mode
    notebook = json.load(f) # Load the JSON content

# Go through each cell and print its type + content
for i, cell in enumerate(notebook.get('cells', []), 1): # Enumerate through each cell in the notebook
    cell_type = cell.get('cell_type') # Get the type of the cell
    source = ''.join(cell.get('source', []))  # source is a list of lines

    print(f"\n=== Cell {i} ({cell_type.upper()}) ===\n") # Print cell number and type
    print(source) # Print the content of the cell
    
    # If the cell is a code cell, print the outputs
    if cell_type == 'code': # Check if the cell is a code cell
        outputs = cell.get('outputs', []) # Get the outputs of the cell
        for j, output in enumerate(outputs, 1): # Enumerate through each output
            print(f"\n--- Output {j} ---") # Print output number
            if 'text' in output: # Check if 'text' is in the output
                print(''.join(output['text'])) # Print the text output
            elif 'data' in output: # Check if 'data' is in the output
                if 'text/plain' in output['data']: # Check if 'text/plain' is in the data
                    print(''.join(output['data']['text/plain'])) # Print the text data
                elif 'image/png' in output['data']: # Check if 'image/png' is in the data
                    print("[Image output: PNG]") # Print image output type
                elif 'text/html' in output['data']: # Check if 'text/html' is in the data
                    print("[HTML output]") # Print HTML output type
                else: # If the data type is not recognized
                    print("[Other data type]") # Print other data type
            else: # If the output type is not recognized
                print("[Unknown output type]") # Print unknown output type

    print("\n" + "="*50) # Print separator line

print("\nFinished extracting notebook contents.") # Print completion message



# End



