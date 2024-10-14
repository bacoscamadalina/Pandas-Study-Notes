import pandas as pd

org = pd.read_csv('organizations-100.csv')

print('/////RENAMING/////')

orgrenam = org.rename(columns={'Points': 'Score'})
print(orgrenam.head(5))

print(70 * '-')

orgrenind = org.rename(index={0: 'firstEntry'})
print(orgrenind.head(5))

print(70 * '-')

orgaxis = org.rename_axis('Company', axis='rows').rename_axis('Fields', axis='columns')
print(orgaxis.head(5))

print('/////COMBINING/////')
'''
- concat()
- join()
- merge()
'''

data1 = {
    'id': ['0', '1', '2', '3', '4'],
    'Name': ['Anna', 'Bert', 'Jack', 'David', 'Emil'],
    'Shift': ['Nigth', 'Day', 'Day', 'Night', 'Day']
}

data2 = {
    'id': ['5', '6', '7', '8', '9'],
    'Name': ['Andrew', 'Sarah', 'Elly', 'Dominic', 'Ray'],
    'Shift': ['Nigth', 'Night', 'Day', 'Day', 'Nigth']
}

d1 = pd.DataFrame(data1, columns=['id', 'Name', 'Shift'])
d2 = pd.DataFrame(data2, columns=['id', 'Name', 'Shift'])

print(f'Data 1: {d1}')
print(f'Data 2: {d2}')

print(70 * '-')

print('///concat()///')
print(pd.concat([d1,d2]))
print('///join()///')
print(d1.join(d2,lsuffix='_Company1',rsuffix='_Company2'))
