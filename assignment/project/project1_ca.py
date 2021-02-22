
from nsepy import get_history
import talib as ta
from datetime import date
import numpy as np
import pandas as pd


stock_list=["ASIANPAINT","AXISBANK","BAJAJ-AUTO","BAJFINANCE","BAJAJFINSV","BPCL","BHARTIARTL","BRITANNIA","CIPLA","COALINDIA","DIVISLAB","DRREDDY",
"EICHERMOT","GAIL","GRASIM","HCLTECH","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDUNILVR",
"HDFC","ICICIBANK","ITC","IOC","INDUSINDBK","INFY","JSWSTEEL","KOTAKBANK","LT","M&M","MARUTI",
"NTPC","NESTLEIND","ONGC","POWERGRID","RELIANCE","SBILIFE","SHREECEM","SBIN","SUNPHARMA","TCS",
"TATAMOTORS","TATASTEEL","TECHM","TITAN","UPL","ULTRACEMCO","WIPRO"]
# print(len(stock_list))


data_1=[]
data_1=pd.DataFrame(data_1)

for i in stock_list:
	data=get_history(symbol=i,start=date(2020,1,1),end=date(2021,2,5))
	data = pd.DataFrame(data)
	data_1 = pd.concat([data_1,data])
data_1["Date"]=data_1.index
data_1.set_index(["Symbol","Date"],inplace=True)


data_1["sma_20"]=data_1["Close"].apply(lambda x: ta.SMA(x,timeperiod=20))
data_1["sma_50"]=data_1["Close"].apply(lambda x: ta.SMA(x,timeperiod=50))
print(data_1)
# data_1["Signal"]=data_1.apply(lambda x: 1 if data_1["sma_20"]>data_1["sma_50"] else 0)




# df=data_1.groupby(level="Symbol").Close.apply(lambda x:ta.SMA(x,timeperiod=20))
# data_2=data_1.join(df.rename("sma_20"))
# df=data_1.groupby(level="Symbol").Close.apply(lambda x:ta.SMA(x,timeperiod=50))
# data_2=data_2.join(df.rename("sma_50"))



# data_2.loc[data_2["sma_20"]>data_2["sma_50"],"Signal"]=1
# data_2.loc[data_2["sma_20"]<data_2["sma_50"],"Signal"]=0
# data_2["Signal_1"]=data_2.Signal.shift(1)
# data_2["postion"]=df["Signal"]-df["Signal_1"]

# data_2=data_2.assign(postion=lambda x:(x["Signal"]-x["Signal_1"]))


# print(data_2.loc["ASIANPAINT"]["postion"]==1)

# df=data_2.groupby(level="Symbol").apply(lambda x:1 if  data["sma_20"] > data["sma_50"]else 0)
# data_3=data_2.join(df.rename("postion"))


# print(data_1.index.get_level_values("Date").unique())

# print(data_2.loc[["ASIANPAINT"],["sma_20"]])
# print(data_2.index)
# print(len(data_2.index))

# for i in range(len(data_2.index)):
# 	if data_2["sma_20"][i] >data_2["sma_50"][i]:
		
# 	else:
		
# df=data_2.groupby(["Symbol","sma_50"]).sum()
# print(df)



# df_unstack=data_2.unstack()
# print(df_unstack.loc["ASIANPAINT"])







