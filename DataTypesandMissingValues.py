import pandas as pd

org = pd.read_csv('organizations-100.csv')

# Dtype -> data type for a column in a DataFrame or a Series
print('/////DTYPES/////')

print(70 * '-')
print(f'Points type: {org.Points.dtype}')
print(f'Industry type: {org.Industry.dtype}')
print(70 * '-')
# For every column
print(org.dtypes)
print(70 * '-')

# astype() -> convert a column of one type into another
print(org.Points.astype('float64'))
print(70 * '-')

print('/////MISSING DATA/////')
print(70 * '-')
# isnull() -> To select NaN entries
print(pd.isnull(org.Industry))
print(70 * '-')
# fillna() ->  To replace missing values
print(org.Industry.fillna('Unknown'))
print(70 * '-')
# backfill strategy -> fill each missing value with the first non-null value that appears sometime after the given record in the database
# replace()
print(org.Industry.replace('Automotive', 'Plastics'))
