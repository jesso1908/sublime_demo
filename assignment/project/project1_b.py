"""Pathik Opening Drive"""

from nsepy import get_history
import talib as ta
from datetime import date
import numpy as np
import pandas as pd


df=get_history(symbol="ICICI",start=date(2019,1,1),end=date.today())


open_prices=df["Open"].to_numpy()
high_prices=df["High"].to_numpy()
low_prices=df["Low"].to_numpy()
close_prices=df["Close"].to_numpy()

dates=list(df.index.values)


datelist=[]
for i in range(1,len(dates)):
	datelist.append(dates[i])

"""First Condition"""
signal=[]
for i in range(1,len(open_prices)):
	if(open_prices[i]>high_prices[i-1]) and (open_prices[i]==low_prices[i]):
		signal.append(1)
	elif(open_prices[i]<low_prices[i-1]) and (open_prices[i]==high_prices[i]):
		signal.append(-1)
	else:
		signal.append(0)

dictionary={"date":datelist,"Signal":signal}

"""converting the  dictionary into dataframe """
df=pd.DataFrame(dictionary)
# pd.set_option("display.max_rows",300)
# print(dataframe)

print(df.loc[df['Signal'] == -1])
print(df.loc[df['Signal'] == 1])

