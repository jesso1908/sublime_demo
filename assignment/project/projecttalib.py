## Importing necessary libraries
from nsepy import get_history
import talib as ta
from datetime import date
import numpy as np
import pandas as pd

## Fetching data from nsepy
df=get_history(symbol="SBIN",start=date(2020,1,1),end=date.today())

## Converting data obtained as a dataframe(pandas series) to individual array's using to_numpy()
open_prices=df["Open"].to_numpy()
high_prices=df["High"].to_numpy()
low_prices=df["Low"].to_numpy()
close_prices=df["Close"].to_numpy()

## To get index values of dateframe as list
dates=list(df.index.values)

"""copying only the required values from dates to datelist.
we are starting from date 50 because SMA values start from 50th value onwards"""
datelist=[]
for i in range(50,len(dates)):
	datelist.append(dates[i])

## List created to store sma_20 values.
a=[]
a=ta.SMA(close_prices,timeperiod=20)

## List created to store sma_50 values.
b=[]
b=ta.SMA(close_prices,timeperiod=50)

##list to store RSI values
rsi=[]
rsi=ta.RSI(close_prices,timeperiod=14)
print(rsi)


"""Creating a new list signal such that if 20_day SMA greater than 50_day SMA 
then signal value becomes 1 else if 50_day SMA greater than 20_day SMA then 
signal value becomes 0"""
signal=[]
for i in range(len(a)):
	if a[i]>b[i]:
		signal.append(1)
	else:
		signal.append(0)

""" Creating a new list position whose values are day to day difference of the position list.
Position 1 implies long(signal changed from 0 to 1) 
position -1 implies short(signal changed from 1 to 0)"""
position=[]
for i in range(50,len(signal)):
	position_value=signal[i]-signal[i-1]
	position.append(position_value)

""" Creating a dictionary to view both the order signal and corresponding dates"""
dictionary={"date":datelist,"position":position}

"""converting the  dictionary into dataframe """
dataframe=pd.DataFrame(dictionary)
pd.set_option("display.max_rows",300)
# print(dataframe)

