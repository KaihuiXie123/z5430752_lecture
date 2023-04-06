""" lec_pd_series.py
Companion codes for the lecture on pandas Series
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

# Create a series object
ser = pd.Series(data=prices, index=dates)
print(ser)
# Select Qantas price on '2020-01-02' ($7.16) using the `ser` series
prc1 = ser['2020-01-02']
print(prc1)

# Unlike dictionaries, you can slice a series
prcs = ser['2020-01-06':'2020-01-10']
print(prcs)

# Use `.array` to get the underlying data array
ary = ser.array
print(ary)
# Like any instance, you can get its type (i.e., the class used to create the
# instance)
type(ser.array)

# Use the `index` attribute to get the index from a series
the_index = ser.index
print(the_index)
print('The type of `the_index` is', type(the_index))

# Replace the existing index with another with different values
ser.index = [0, 1, 2, 3, -4, 5, 6, 7, 8, 1000] # Note the -4 and 1000
print(ser)

x = ser[1000]
print(x)
