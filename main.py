# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import numpy

df = pd.read_csv('https://raw.githubusercontent.com/johnpbonner3/practicePokemon/master/pokemon_data.csv')
pd.set_option('display.width', 320)


pd.set_option('display.max_columns',15)
pd.set_option('display.max_rows',400)

# print(df.head(5))

# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))

# df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# print(df.head(5))
#### Read Headers


## Read each Column
#print(df[['Name', 'Type 1', 'HP']])

## Read Each Row
#print(df.iloc[0:4])
# for index, row in df.iterrows():
#     print(index, row['Name'])
#df.loc[df['Type 1'] == "Grass"]

## Read a specific location (R,C)
#print(df.iloc[2,1])

#df.sort_values(['Type 1', 'HP'], ascending=[1,0])

#print(df)

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

#df = df.add(columns=['Total'])

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

#print(df.sort_values(['Total'], ascending=False))

#print(df.head(5))

#df.to_csv('modifiedPokemon.csv')

#print(df.loc[((df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')) | ((df['Type 1'] == 'Poison') & (df['Type 2'] == 'Grass'))])
#print(df.loc[(df['Type 1'] == 'Poison') | (df['Type 2'] == 'Poison')])

poison_DF = df.loc[(df['Type 1'] == 'Poison') | (df['Type 2'] == 'Poison')].reset_index(drop=True, inplace=True)
    #print(poison_DF)
    #This crazy line takes any pokemon that is poison type (See Above line) and sorts them by most hp to least, with the
    #floor of the HP being 70. (And resets index

print(poison_DF.sort_values(['HP'], ascending = False).loc[poison_DF['HP'] > 70])
