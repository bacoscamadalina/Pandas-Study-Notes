import pandas as pd

org = pd.read_csv('organizations-100.csv')

print('////GROUPWISE ANALYSIS////')

print('---GROUPBY()---')
print(org.groupby(
    'Number_of_employees').Number_of_employees.count())  # value_counts() is just a shortcut to this groupby() operation.
print(70 * "-")
print(org.groupby(
    'Country').Points.min())  # min()- returns the minimum value from the Points column for each Country group.
print(70 * "-")
# agg()- method used to apply multiple aggregation functions to each group
print(org.groupby(['Country']).Points.agg(['count', 'max', 'min']))
'''
{
'count': counts how many rows there are for each country in the Points column.
'max': Finds the maximum value of the Points column for each country.
'min': Finds the minimum value of the Points column for each country.
}
'''
print(70 * "-")
print('/////MULTI-INDEXES/////')

org_descr = org.groupby(['Country', 'Industry']).Description.agg(
    [len])  # len- counts how many rows are in the Description column for each group.
print(org_descr)

# Retrieves the index of the org_descr
ind = org_descr.index
print(type(ind))  # MultiIndex -> because it consists of more than one grouping column (Country and Industry).

print(
    org_descr.reset_index())  # reset_index() -> moves the index columns (Country, Industry) back into regular columns of the DataFrame

print(70 * "-")
print('/////SORTING/////')

org_reset = org_descr.reset_index()
print(org_reset.sort_values(by='len', ascending=False))  # ascending=False -> descending sort
print(70 * "-")

# sort by index values
print(org_reset.sort_index())

print(70 * "-")
# sort by more than one column at a time
print(org_reset.sort_values(by=['Country', 'len'], ascending=False))
