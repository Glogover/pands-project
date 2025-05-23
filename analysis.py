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

"""
The Visual Studio Code terminal has a limited scrollback buffer, 
meaning that if a large amount of data is output, older lines will be discarded 
and will no longer be visible.
To increase this limit:
   Navigate to File → Preferences → Settings (or press Ctrl + ,).
   Search for terminal.integrated.scrollback.
By default, this is set to approximately 1000 lines — you can increase it 
to 10,000 or even higher if you need to view extended logs.
"""

print("\n*** Iris Dataset Analysis ***") # Print title
print("\nAuthor: Marcin Kaminski\n") # Print author name
print("\nPlease wait while the analysis is being performed...\n") # Print waiting message


# Import necessary libraries
import pandas as pd # For data manipulation
import matplotlib.pyplot as plt # For plotting
import seaborn as sns # For advanced plotting
import json # For JSON handling
import subprocess # For running shell commands


# Load the dataset
iris = pd.read_csv('iris.csv') # Load the dataset from CSV file
# Sourced from [1]: https://datascienceparichay.com/article/read-csv-files-using-pandas-with-examples/


# Display random sample of the dataset

print("\nRandom sample of the dataset:\n") # Print message
print(iris.sample(10))
# Sourced from [2]: https://www.w3schools.com/python/pandas/ref_df_sample.asp


# 1. Output a summary of each variable to a single text file

summary = iris.drop(columns=['class']).describe() # Drop the 'class' column and get summary statistics
# Sourced from [3]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html

with open('iris_summary.txt', 'w') as f: # Open file in write mode
    f.write(str(summary)) # Write summary to file
print("\nSummary statistics saved to iris_summary.txt") # Print confirmation message
# Sourced from [4]: https://www.geeksforgeeks.org/how-to-open-a-file-using-the-with-statement/

# 2. Save a histogram of each variable to png files

for column in iris.columns: # Loop through each column
    if column == 'class':
        continue # Skip the 'class' column

    plt.figure(figsize = (8, 6)) # Create a new figure with specified size
    # Sourced from [5]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html

    sns.histplot(iris[column], kde=True) # Plot histogram with kernel density estimate
    # Sourced from [6]: https://seaborn.pydata.org/generated/seaborn.histplot.html

    plt.title(f'Histogram of {column}') # Set title
    # Sourced from [7]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html

    plt.xlabel(column) # Set x axis label
    # Sourced from [8]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html

    plt.ylabel('Frequency') # Set y axis label
    # Sourced from [9]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html

    plt.grid(True) # Show grid
    # Sourced from [10]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html

    plt.tight_layout() # Adjust layout to avoid label cutoff
    # Sourced from [11]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html

    plt.savefig(f'{column}_histogram.png') # Save figure to file
    # Sourced from [12]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

    plt.close() # Close the figure
    # Sourced from [13]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html

    print(f"Saved histogram: {column}_histogram.png") # Print confirmation message

# 3. Output a scatter plot of each pair of variables
    
numeric_columns = iris.select_dtypes(include=['float64', 'int64']).columns # Select numeric columns
# Sourced from [14]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html

for i, col1 in enumerate(numeric_columns): # Loop through each numeric column
    # Sourced from [15]: https://docs.python.org/3.12/library/functions.html#enumerate

    for col2 in numeric_columns[i+1:]: # Loop through each subsequent numeric column
        plt.figure(figsize=(8, 6)) # Create a new figure with specified size
        sns.scatterplot(data = iris, x = col1, y = col2, hue='class') # Create scatter plot with hue based on 'class'
        # Sourced from [16]: https://seaborn.pydata.org/generated/seaborn.scatterplot.html

        plt.title(f'Scatter plot of {col1} vs {col2}') # Set title
        plt.xlabel(col1) # Set x axis label
        plt.ylabel(col2) # Set y axis label
        plt.grid(True) # Show grid
        plt.tight_layout() # Adjust layout to avoid label cutoff
        plt.savefig(f'{col1}_{col2}_scatter_plot.png') # Save figure to file
        plt.close() # Close the figure
        print(f"Saved scatter plot: {col1}_{col2}_scatter_plot.png") # Print confirmation message

# 4. Perform any other analysis appropriate
        
print('\nFor further analysis, please refer to the Jupyter notebook analysis.ipynb, which also is displayed below in the terminal.\n') # Print message for additional analysis



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



