import pandas as pd

from pathlib import Path

p = Path(__file__)
data_path = str(p.cwd())+'\data\\'

file_input = data_path+'data_input.csv'

df = pd.read_csv(file_input)

print(type(df))
print(type(df['email']))
df['domain'] = df['email'].apply(lambda x : x.split('@')[1])
print(df['domain'].value_counts(normalize=True).plot())
print(df['domain'].info())

# d = {'a': 1, 'b': 2, 'c': 3}
# ser = pd.Series(data=d, index=['a', 'b', 'c'])


# print(ser.apply(lambda x: x*2))