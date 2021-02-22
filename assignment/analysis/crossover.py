import pandas as pd 
import talib as ta
import numpy as np
df=pd.read_csv("E:/sublime/intraday data/Upto 2011/NIFTY upto 2011/UPTO 2011 NIFTY.txt",parse_dates=[[1,2]])
df.columns=["Datetime","SYMBOL","open","high","low","close"]
del df["SYMBOL"]
df["Datetime"]=pd.to_datetime(df["Datetime"])
df=df.set_index(df["Datetime"])
del df["Datetime"]
df_1=pd.DataFrame(df)
# print(df_1)

open_prices=df["open"].to_numpy()
high_prices=df["high"].to_numpy()
low_prices=df["low"].to_numpy()
close_prices=df["close"].to_numpy()

a=[]
a=ta.SMA(close_prices,timeperiod=20)

b=[]
b=ta.SMA(close_prices,timeperiod=50)
rsi=[]
rsi=ta.RSI(close_prices,timeperiod=14)
signal=[]
for i in range(len(a)):
	if a[i]>b[i]:
		signal.append(1)
	else:
		signal.append(0)
print(len(signal))
position=[]
for i in range(1,len(signal)):
	position_value=signal[i]-signal[i-1]
	position.append(position_value)
print(len(position))

Orders=[]
for i in range(len(position)):
	if position[i]==1 and rsi[i]>50:
		Orders.append(1)
	elif position[i]==-1 and rsi[i]<50:
		Orders.append(-1)
	else:
		Orders.append(0)
# print(Orders)
# print(len(Orders))
orders=np.array(Orders)
df["orders"]=orders[5]

print(df["orders"])

