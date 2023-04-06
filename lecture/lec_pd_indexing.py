""" lec_pd_indexing.py
Companion codes for the lecture on indexing pandas objects
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

# Trading day counter
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

# Create a series object
ser = pd.Series(data=prices, index=dates)
print(ser)
# Data Frame with close and Bday columns
df = pd.DataFrame(data={'Close': ser, 'Bday': bday}, index=dates)
print(df)
# Set `x` below to be the price on 2020-01-10
x = ser.loc['2020-01-10'] # --> 7.0

ser2 = ser.copy()
print(ser2)
# Set the price for 2020-01-02 to zero
ser2.loc['2020-01-02'] = 0
print(ser2)
x = ser.loc[['2020-01-03', '2020-01-10']]
print(x)
print(type(x)) # --> <class 'pandas.core.series.Series'>

x = ser.loc['2020-01-03':'2020-01-10']
print(x)

# For instance, selecting the close price on January 3, 2020
x = df.loc['2020-01-03', 'Close']
print(x) # --> 7.19
x = df.loc[:, 'Close']
print(x)
type(df.loc[:, 'Close']) # --> <class 'pandas.core.series.Series'>

y = df.loc['2020-01-03', :]
print(y)
print(type(df.loc['2020-01-03', :])) # --> <class 'pandas.core.series.Series'>

x = df.loc['2020-01-03']
print(x)
print(type(df.loc['2020-01-03'])) # --> <class 'pandas.core.series.Series'>

x = df.loc[['2020-01-02', '2020-01-03'], 'Close']
print(x)

x = df.loc['2020-01-01':'2020-01-10', :]
print(x)
print(type(x)) # --> <class 'pandas.core.frame.DataFrame'>
x = df.loc['2999-01-01':'2999-01-10', :]
print(x)
print(type(x)) # --> <class 'pandas.core.frame.DataFrame'>

x = df.loc['2020-01-06':, :]
print(x)
x = df.loc['2020-01-06', 'Close':]
print(x)

df2 = df.copy()
df2.rename(index={'2020-01-08':'1900-01-01'}, inplace=True)
print(df2)
x = df2.loc['2020-01-03':'2020-01-10', :]
print(x)
# You can avoid these issues by sorting the dataframe first
df2.sort_index(inplace=True)
x = df2.loc['2020-01-03':'2020-01-10', :]
print(x)

# This will return a DataFrame
x = df.loc['2020-01-03':'2020-01-03']
print(x)
# This will return a series
x = df.loc['2020-01-03']
print(x)
print(type(x)) # -->  <class 'pandas.core.series.Series'>


# ser.iloc[pos] --> scalar if abs(pos) < len(ser), otherwise error
x = ser.iloc[0]  # --> 7.16
x = ser.iloc[-1] # --> 7.04

# Copy the series
s2 = ser.copy()
# assign
s2.iloc[0] = 0
print(s2)

x = ser.iloc[[0, 2]]
print(x)
x = ser.iloc[0:1]  # x --> series with one row
print(x)
x = ser.iloc[0:2]
print(x)

# df.iloc[row pos] --> series if abs(pos) < len(df.index)
# --> series with elements from the first "row" -- column labels as row indexes
x = df.iloc[0]
print(x)
# Equivalent to
x = df.iloc[0, :]
print(x)
# First column (and all rows):
x = df.iloc[:, 0]
print(x)
# This will return a series with the first two columns as labels:
x = df.iloc[0, [0, 1]]
print(x)
# This will return a *dataframe* with the first row of df
x = df.iloc[0:1, :]
print(x)
# Note: will raise IndexError if pos is out of bounds
x = df.iloc[[0, 1]]  # --> DF with first two rows of df
print(x)

x = df.iloc[1:1000, :]
print(x)
x = df.iloc[999:1000, :]
print(x)
# Slices can be open ended
x = df.iloc[2:, :]
print(x)
x = df.iloc[0, 0:]
print(x)
# This will return an empty series
x = df.iloc[0, 10:]
print(x)

print(ser)
# Set `x` to be the price for '2020-01-13'
x = ser['2020-01-13']
print(x) # --> 7.02
# Set `x` to be a series with the first two rows of `ser`
x = ser[['2020-01-02', '2020-01-03']] # --> first two rows
# Set `x` to include all obs between  '2020-01-13' and '2020-01-14'
x = ser['2020-01-13':'2020-01-14']
print(x)
x = ser['2020-01-13':'3000-01-01']
print(x)

# Create a series with an unsorted index
new_ser = pd.Series(data=[1,3,2], index=['a', 'c', 'b'])
x = new_ser['a':'b']
print(x)
sorted_ser = new_ser.sort_index()
print(sorted_ser)
# This will return only the first rows (not the entire series as before)
x = sorted_ser['a':'b']
print(x)
x = sorted_ser['b':'z']
print(x)

print(ser)
# Get the first element of the series
x = ser[0]
# Get the first and fourth element (series)
x = ser[[0, 3]]
# NOTE: When using slices, the endpoints are NOT included
# This will return a series with the first element only
x = ser[0:1]
print(x)
# This will return the first five elements of the series
x = ser[:5]
print(x)
# This will return every other element, starting at position 0
x = ser[::2]
# This returns the series in reverse order
x = ser[::-1]

new_ser = pd.Series(data=['a', 'b', 'c'], index=[1, -4, 10])
# This will produce an empty series (because pandas thinks these are positions, not labels)
x = new_ser[1:-4]
print(x)

print(df)
x = df['Close']
print(x)
print(type(df["Close"]))
cols = ['Close', 'Bday']
print(df[cols])
# We can pass the list of columns directly to the DataFrame:
print(df[["Close", "Bday"]])
print(type(df[["Close", "Bday"]]))
# <class 'pandas.core.frame.DataFrame'>
x = df['Close': 'Bday']
print(x)
# x --> dataframe with first two rows
x = df['2020-01-02':'2020-01-03']
print(x)
# x --> all rows but the last one
x = df[:-1]
print(x)
# x -> returns empty DF
x = df[100:1001]
print(x)