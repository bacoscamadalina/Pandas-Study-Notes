import pandas as pd

ecosurvey = pd.read_csv('economic-survey-of-manufacturing-june-2024-csv.csv')
print(ecosurvey.head())
print(70 * '-')
# SELECTING

print("//////Period DATA - EX1//////")
print(ecosurvey.Period)
print("//////Period DATA - EX2//////")
print(ecosurvey['Period'])

print(70 * '-')

print("//////Series_title_1 DATA//////")
print(ecosurvey.Series_title_1)
print(f'Data1 : {ecosurvey.Series_title_1[0]}')

print(70 * '-')

# INDEXING
'''
ACCESSOR OPERATORS : loc / iloc (row first - column second)

ILOC -> Index-based selection: selecting data based on its numerical position in the data.
LOC -> Label-based selection
'''

# Index-based selection

print('//////INDEX-BASED SELECTION//////')
print(ecosurvey.iloc[0])
print(70 * '-')

# Get a column
print('COLUMN')
print(ecosurvey.iloc[:, 0])
print('First 3 columns')
print(ecosurvey.iloc[:3, 0])
print('2nd and 3rd entries')
print(ecosurvey.iloc[1:3, 0])
print('Passing a list')
print(ecosurvey.iloc[[0, 1, 2], 0])
print('Last 5 elements')
print(ecosurvey.iloc[-5:])
print(70 * '-')

print('//////LABELD-BASED SELECTION//////')
print('First entry')
print(ecosurvey.loc[0, 'Series_reference'])
print(ecosurvey.loc[:, ['Period', 'Magnitude', 'UNITS']])
print(70 * '-')

print('//////MANIPULATING THE INDEX//////')
print(ecosurvey.set_index('Period'))
print(70 * '-')

print('//////CONDITIONAL SELECTION//////')
print(ecosurvey.Series_reference == 'MFGQ.SFA1CA')
# AND
print(ecosurvey.loc[(ecosurvey.Series_reference == 'MFGQ.SFA1CA') & (ecosurvey.Period == 1992.12)])
# OR
print(ecosurvey.loc[(ecosurvey.Series_reference == 'MFGQ.SFA1CA') | (ecosurvey.Period == 1992.12)])
# isin()
print(ecosurvey.loc[ecosurvey.Series_reference.isin(['MFGQ.SFA1CA', 'MFGQ.SFZ2CA'])])
# notnull()
print(ecosurvey.loc[ecosurvey.Suppressed.notnull()])
print(70 * '-')

print('//////ASSIGNING DATA//////')
ecosurvey['Period'] = 2024
print(ecosurvey['Period'])

ecosurvey['index_backwards'] = range(len(ecosurvey), 0, -1)
print(ecosurvey['index_backwards'])
