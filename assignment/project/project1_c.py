"""Pathik Reversal Setup"""
from nsepy import get_history
import talib as ta
from datetime import date
import numpy as np
import pandas as pd


stock_list=["ASIANPAINT","AXISBANK","BAJAJ-AUTO",
"BAJFINANCE",
"BAJAJFINSV",
"BPCL",
"BHARTIARTL",
"BRITANNIA",
"CIPLA",
"COALINDIA",
"DIVISLAB",
"DRREDDY",
"EICHERMOT",
"GAIL",
"GRASIM",
"HCLTECH",
"HDFCBANK",
"HDFCLIFE",
"HEROMOTOCO",
"HINDALCO",
"HINDUNILVR",
"HDFC",
"ICICIBANK",
"ITC",
"IOC",
"INDUSINDBK",
"INFY",
"JSWSTEEL",
"KOTAKBANK",
"LT",
"M&M",
"MARUTI",
"NTPC",
"NESTLEIND",
"ONGC",
"POWERGRID",
"RELIANCE",
"SBILIFE",
"SHREECEM",
"SBIN",
"SUNPHARMA",
"TCS",
"TATAMOTORS",
"TATASTEEL",
"TECHM",
"TITAN",
"UPL",
"ULTRACEMCO",
"WIPRO"]
def sma_20():

	a=ta.SMA(close_prices,timeperiod=20)

data_1=[]
data_1=pd.DataFrame(data_1)

for i in stock_list:
	data=get_history(symbol=i,start=date(2020,1,1),end=date(2021,2,5))
	data = pd.DataFrame(data)
	data_1 = pd.concat([data_1,data])
data_1["Date"]=data_1.index
data_1.set_index(["Symbol","Date"],inplace=True)
# print(data_1)
# df= data_1.groupby(level="Symbol").Close.apply(lambda x: if ta.SMA(x,timeperiod=20) > ta.SMA(x,timeperiod=50)
# 	else False )
# def cross_over(x):
# 	if ta.SMA(timeperiod=20)> ta.SMA(timeperiod=50):



df=data_1.groupby(level="Symbol").Close.apply(lambda x:ta.SMA(x,timeperiod=20))
data_2=data_1.join(df.rename("sma_20"))
df=data_1.groupby(level="Symbol").Close.apply(lambda x:ta.SMA(x,timeperiod=50))
data_2=data_2.join(df.rename("sma_50"))

print(data_2.loc["ASIANPAINT"])




# df=data_1.groupby(['Symbol',"Date_1"]).Close.mean()
# # print(df)
# print(type(df))
# print(df.loc["WIPRO"])
# df_1=df["Close"]
# print(df_1)
# print(type(df_1))
# print(df.unstack())


