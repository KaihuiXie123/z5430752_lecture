""" lec_pd_dataframes.py
Companion codes for the lecture on Dataframes
"""

import pandas as pd


# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

# Close prices
prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# Business (trading) day counter
bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]

# Series with prices
prc_ser = pd.Series(data=prices, index=dates)

# Series with trading day
bday_ser = pd.Series(data=bday, index=dates)

# Data Frame with close and Bday columns
df = pd.DataFrame({'Close': prc_ser, 'Bday': bday_ser})
print(df)

other_dates = [
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  '2020-01-16',
  '2020-01-17',
  ]
other_bday = [
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        ]
new_bday_ser = pd.Series(data=other_bday, index=other_dates)
new_df = pd.DataFrame({'Close': prc_ser, 'Bday': new_bday_ser})
print(new_df)
# The attribute `columns` returns the column index
print(df.columns)
print(type(df.columns))

col0 = df['Close']
print(col0)
print(type(col0))

print(col0.index)
print(type(col0.index))
print(df.index)
print(type(df.index))

df.columns = ['A', 'B']
df.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(df)

df.columns = ['Close', 'Bday']
df.index = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]
print(df)

# Create a series with an unsorted index
new_ser = pd.Series(data=[1,3,2], index=['a', 'c', 'b'])
# This will return 'False'
print(new_ser.is_monotonic_increasing)

# Sort the series
sorted_ser = new_ser.sort_index()
print(sorted_ser)
# This will return only the first rows (not the entire series as before)
x = sorted_ser['a':'b'] # --> only first two rows
print(x)

# Create a series with an unsorted index
ser_sort_inplace = pd.Series(data=[1,3,2], index=['a', 'c', 'b'])
# Sort the series. Note that we are not assigning this function call
# to a new variable.
ser_sort_inplace.sort_index(inplace = True)
print(ser_sort_inplace)