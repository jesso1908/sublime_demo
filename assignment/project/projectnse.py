from nsepy import get_history
from datetime import date
import numpy as np
import pandas as pd
df=get_history(symbol="SBIN",start=date(2021,1,1),end=date.today())
open_prices=df["Open"].to_numpy()
high_prices=df["High"].to_numpy()
low_prices=df["Low"].to_numpy()
close_prices=df["Close"].to_numpy()
mid_point=[] ## midpoint of open and close
for i in range(len(open_prices)):
	point=(open_prices[i]+close_prices[i])/2
	mid_point.append(point)
dates=df.index.values

# dates=df["Date"].strftime("%Y:%m:%d")
# dates=df.index.to_numpy()
# print(dates)


def is_bullishengulfing(open_1,high,low,close):
	bullish_engulfinglist=[False]
	for i in range(1,len(open_1)):
		if(open_1[i-1]>close[i-1]) and (close[i]>open_1[i-1]) and (open_1[i]<close[i-1]):
			bullish_engulfinglist.append(True)
		else:
			bullish_engulfinglist.append(False)
 	
	return bullish_engulfinglist
a=is_bullishengulfing(open_prices,high_prices,low_prices,close_prices)
print("Bullish engulfing\n")
a_1=zip(dates,a)
a_2=list(a_1)
print(a_2)


def is_bearishengulfing(open_1,high,low,close):
	bearish_engulfinglist=[False]
	for i in range(1,len(open_1)):
		if(open_1[i-1]<close[i-1]) and (open_1[i]>close[i-1]) and (close[i]<open_1[i-1]):
			bearish_engulfinglist.append(True)
		else:
			bearish_engulfinglist.append(False)
	return bearish_engulfinglist
b=is_bearishengulfing(open_prices,high_prices,low_prices,close_prices)
print("\nBearish engulfing\n",b)

def is_insidebar(open_1,high,low,close):
	inside_barlist=[False]
	for i in range(1,len(open_1)):
		if(high[i]<high[i-1]) and (low[i]>low[i-1]):
			inside_barlist.append(True)
		else:
			inside_barlist.append(False)
	return inside_barlist
c=is_insidebar(open_prices,high_prices,low_prices,close_prices)
print("\nInside bar\n",c)

def is_bullishharami(open_1,high,low,close):
	bullish_haramilist=[False]
	for i in range(1,len(open_1)):
		if(open_1[i-1]>close[i-1]) and (open_1[i]<close[i-1]) and (close[i]>open_1[i-1]):
			bullish_haramilist.append(True)
		else:
			bullish_haramilist.append(False)
	return bullish_haramilist
d=is_bullishharami(open_prices,high_prices,low_prices,close_prices)
print("bullish harami \n",d)

def is_bearishharami(open_1,high,low,close):
	bearish_haramilist=[False]
	for i in range(1,len(open_1)):
		if(open_1[i-1]<close[i-1]) and (open_1[i]>close[i-1]) and (close[i]<open_1[i-1]):
			bearish_haramilist.append(True)
		else:
			bearish_haramilist.append(False)
	return bearish_haramilist
e=is_bearishharami(open_prices,high_prices,low_prices,close_prices)
print("\nBearish harami\n",e)

def is_darkcloud(open_1,high,low,close,mid_point):
	dark_cloudlist=[False]
	for i in range(1,len(open_1)):
		if(open_1[i-1]<close[i-1]) and (open_1[i]>high[i-1] and close[i]<mid_point[i-1] ):
			dark_cloudlist.append(True)
		else:
			dark_cloudlist.append(False)
	return dark_cloudlist
f=is_darkcloud(open_prices,high_prices,low_prices,close_prices,mid_point)
print("\n Dark cloud\n",f)

def is_risingsun(open_1,high,low,close,mid_point):
	rising_sunlist=[False]
	for i in range(1,len(open_1)):
		if(open_1[i-1]>close[i-1]) and (open_1[i]<low[i-1] and close[i]>mid_point[i-1]):
			rising_sunlist.append(True)
		else:
			rising_sunlist.append(False)
	return rising_sunlist
g=is_risingsun(open_prices,high_prices,low_prices,close_prices,mid_point)
print("\n Rising sun\n",g)