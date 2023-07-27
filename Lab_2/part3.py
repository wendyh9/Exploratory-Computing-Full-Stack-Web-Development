import pandas as pd

data = pd.read_csv('weather_data.txt', skipinitialspace = True)
df = pd.DataFrame(data)

# print(data)

# how to print data types of columns in a data frame
# print(data.dtypes)

# how to get a preview of text/csv file
# df.head()


# a. What day(s) had the highest actual precipitation?

# largest val in actual_percipitation col
max_actual_percipitation = df['actual_precipitation'].max()

# row(s) that include the largest val in actual_percipitation
df.loc[df['actual_precipitation'] == max_actual_percipitation]

# date(s) when largest val in actual_percipitation occurred
print('Part a: date(s) when largest val in actual_percipitation occurred') 
print(df['date'][df['actual_precipitation'] == max_actual_percipitation])
print('\n')


# b. What was the average actual max temp for July 2014?
print('Part b: average actual max temp for July 2014')
print(df[df['date'].between('2014-7-1', '2014-7-31')]['actual_max_temp'].mean())
print('\n')


# c. What days was the actual max temp the record max temp?
print('Part c: days when actual max temp was record max temp')
print(df['date'][df['actual_max_temp'] == df['record_max_temp']])
print('\n')


# d. How much did it rain in October 2014?
print('Part d: total rain in October 2014')
print(df[df['date'].between('2014-10-1', '2014-10-31')]['actual_precipitation'].sum())
print('\n')


# e. What day(s), if any, was the actual low temperature below 60 degrees and actual max temperature above 90 degrees on the same day?
print('Part e: when actual low temperature below 60 degrees and actual max temperature above 90 degrees on same day (if any day(s))')
print(df['date'][(df['actual_min_temp'] < 60) & (df['actual_max_temp'] > 90)])
print('\n')