# Pandas = Python Library for data analysis

import pandas as pd

'''
Core objects : DataFrame/Series
DataSeries -> a table
Series -> sequence of data values ( = a list)
'''

# WRITING DATA FILES

# DataFrame
dataframe = pd.DataFrame({
    'Price ($)': [150, 180],
    'DepoQuantity': [3, 2]},
    index=['Table', 'Chair']
)

print('DataFrame example:')
print(dataframe)

# Series
series = pd.Series([140, 220, 325, 410], index=['Price 2013', 'Price 2014', 'Price 2015', 'Price 2016'], name='Chair')
print(f'Series example:')
print(series)

# READING DATA FILES

print('Reading Data Files')
ecosurvey = pd.read_csv('economic-survey-of-manufacturing-june-2024-csv.csv')
# Checking how large the resulting DataFrame is (records,columns)
print(ecosurvey.shape)

# Examine the content -> first 5 rows
print(ecosurvey.head())
