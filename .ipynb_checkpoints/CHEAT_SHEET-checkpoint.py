####################################################################
# Python PEP Club - Pandas Training Beginners               ########
# by Mat and TJ                                             ########
# 2021-05-13                                                ########
####################################################################

# import modules
import pandas as pd
import os

# print working directory
print(os.getcwd())
# Connect to TEXT/CSV file
df = pd.read_csv('pokemon.csv')
# Connect to EXCEL file
df = pd.read_excel('pokemon.xlsx', sheet_name='sheet1')

# Display the Data [Columns, Head, Tail, Index, Types]
print("Printing Head...")
print(df.head(10))
print("\nPrinting Tail...")
print(df.tail(10))
print("\nPrinting Columns...")
print(df.columns)
print("\nPrinting Indexes...")
print(df.index)
print("\nPrinting Dtypes...")
print(df.dtypes)
print("\nPrinting Describe...")
print(df.describe)
print("\nPrinting NUnique...")
print(df.nunique)

    ######################## Challenge Question ########################
    # Try printing out the last 100 rows excluding the last 10
    # soln: df.tail(100).head(90)
    
    # Try printing out the first 2 columns
    # soln: df.columns[:2]
    
    # Try printint out the dtypes for the last 2 columns
    # soln: df.dtypes[-2:]
    ####################################################################

# Index the Data [Column Indexing, Row Indexing, Index, Find Data by row, column]]
print("\nIndexing a Column...")
print(df['abilities'])
print(df.abilities)
print("\nFirst 10 Rows from abilities column...")
print(df.loc[:10,['abilities']])
print("\nFiltering for our favorite pokemon: Squirtle")
print(df[df['name']=='Squirtle'])
print("\nFilter for Beast Boost abilities")
print(df[['Beast Boost' in l for l in df['abilities']]])

    ######################## Challenge Question ########################
    # find the stats on your favorite pokemon 
    # soln: df[df['name']=='Squirtle']
    
    # Filter for the first 10 rows on the last 4 columns
    # soln: print(df.loc[:10,df.columns[-4:]])
    
    # Create a new column that outputs True for abilities with Blaze and False for abilities without blaze
    # soln: df['blaze_ind'] = ['Blaze' in l for l in df['abilities']]
    ####################################################################

# Modify the Column
df['base_happiness'] = df['base_happiness'] + 1

# Create New Column for the sum, avg, and stdev of legendaries
df['legendary_sum'] = df['is_legendary'].sum()
df['legendary_sum'] = df['is_legendary'].mean()
df['legendary_sum'] = df['is_legendary'].std()

    ######################## Challenge Question ########################
    # trim the data set down to only legendary pokemon
    # df = df[df.is_legendary == 1]
    
    # sum up the against_bug column
    # soln: df['against_bug'].sum()
    
    # avg up the the against_dark column
    # soln: df['against_dark'].mean()
    
    # std dev the against_fairy_column
    # soln: df['against_fairy'].std()
    ####################################################################

# Clean the Data [What to do with NaN and Nulls and 0s]
print(df.isna().sum())
print(df.isnull().sum())
print(df.fillna('N'))

# Output as TEXT/CSV file
df.to_csv('pokemon_out.csv')
# Output as EXCEL file
df.to_excel('pokemon_out.xlsx', sheet_name="sheet1")