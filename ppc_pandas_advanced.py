####################################################################
# Python PEP Club - Pandas Training Beginners               ########
# by Mat and TJ                                             ########
# 2021-06-24                                                ########
####################################################################

'''
    [Agenda]
1. Spyder IDE
2. Import Data with Excel
3. Vlookup in Excel
4. Merge Excel Data in Python
5. Apply a marvelous Lambda Function
'''


# import modules
import pandas as pd
import os

# print working directory
print(os.getcwd())

# Connect to TEXT/CSV file
# df = pd.read_csv('pokemon.csv')

# Connect to EXCEL file
df1 = pd.read_excel('pokemon.xlsx', sheet_name='sheet1')
df2 = pd.read_excel('pokemon.xlsx', sheet_name='sheet2')

# Merge on Evolution to see which pokemon it evolves to
df3 = df1.merge(df2, left_on='name', right_on='name', how='left')


    ######################## Challenge Question ########################
    # Can you find the duplicate join?
    # hint: df5 = df3['evolution'].dropna().sort_values()
    ####################################################################

# Apply lambda to see which pokemon would get KOd for 155 damage
df3['KO'] = df3['hp'].apply(lambda x: x<155)

# Apply with external Function
def size(a):
    if a > 300:
        return('Really Big')
    elif a > 150:
        return('Big')
    elif a > 50:
        return('Average')
    else:
        return('Small')
    
df3['is_large'] = df3['weight kg'].apply(size)

    ######################## Challenge Question ########################
    # Can you group the height of the pokemon?
    ####################################################################

# Delete Data Frame
del df2


######## BEGGINER CODE BELOW ########
'''
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
    
    # Try printing out the first 2 columns
    
    # Try printint out the dtypes for the last 2 columns
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
    
    # Filter for the first 10 rows on the last 4 columns
    
    # Create a new column that outputs True for abilities with Blaze and False for abilities without blaze
    ####################################################################

# Modify the Column
df['base_happiness'] = df['base_happiness'] + 1

# Create New Column for the sum, avg, and stdev of legendaries
df['legendary_sum'] = df['is_legendary'].sum()
df['legendary_sum'] = df['is_legendary'].mean()
df['legendary_sum'] = df['is_legendary'].std()

    ######################## Challenge Question ########################
    # trim the data set down to only legendary pokemon
    
    # sum up the against_bug column
    
    # avg up the the against_dark column
    
    # std dev the against_fairy_column
    ####################################################################

# Clean the Data [What to do with NaN and Nulls and 0s]
print(df.isna().sum())
print(df.isnull().sum())
print(df.fillna('N'))

# Output as TEXT/CSV file
df.to_csv('pokemon_out.csv')
# Output as EXCEL file
df.to_excel('pokemon_out.xlsx', sheet_name="sheet1")
'''