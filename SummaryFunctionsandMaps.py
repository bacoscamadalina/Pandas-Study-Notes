import pandas as pd

ecosurvey = pd.read_csv('economic-survey-of-manufacturing-june-2024-csv.csv')

# describe()
print(f'//////describe() FUNCTION//////')
print(ecosurvey.Period.describe())

print(70*"-")

# mean()
print(f'//////mean() FUNCTION//////')
print(ecosurvey.Period.mean())  # mean value

print(70*"-")

# unique()
print(f'//////unique() FUNCTION//////')
print(ecosurvey.Period.unique())

print(70*"-")

# value_counts() - shows unique values and how often they occur in the dataset
print(f'//////value_counts() FUNCTION//////')
print(ecosurvey.Period.value_counts())

print(70*"-")

# map()
print(f'//////map() FUNCTION//////')
ecosurv_Period_mean= ecosurvey.Period.mean()
print(ecosurvey.Period.map(lambda p: p - ecosurv_Period_mean))
# or
print(ecosurvey.Period - ecosurv_Period_mean)

# apply()
def remean_points(row):
    row.Period = row.Period - ecosurv_Period_mean
    return row

print(ecosurvey.apply(remean_points,axis='columns'))




