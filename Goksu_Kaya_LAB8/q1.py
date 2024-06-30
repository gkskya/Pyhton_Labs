import pandas as pd
import numpy as np

DF14_15 = pd.read_excel('education_gdp_2014_15.xlsx')
DF_13 = pd.read_excel('education_gdp_2013.xlsx')

print('2014_15 Data:')
print(DF14_15)

print('2013 Data:')
print(DF_13)


data= pd.merge(left = DF_13, right = DF14_15, left_on = 'Country Name', right_on = 'Country Name')
print('\nMerged Data Set: ')
print(data)

data= data.replace('..', np.NaN)


print('\nData Set after Replace: ')
print(data)


data= data.dropna()
print('\nData Set after Dropping NaN: ')
print(data)


data['Mean'] = np.mean(data,axis=1)
print('\nData Set with Mean: ')
print(data)

data_all = data.sort_values('Mean')
print('\nSorted by Mean: ')
print(data)

