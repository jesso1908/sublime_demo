import pandas as pd 
from datetime import time,datetime,date,timedelta

df=pd.read_csv("E:/sublime/intraday data/2014/Nifty/uncleaned.csv",parse_dates=[["date","time"]])
# df=df.resample("5T",axis=0).agg({"open":"first","high":"max","low":"min","close":"last"})
df["date_time"]=df["date_time"] - timedelta(hours=0,minutes=1)
df=df.set_index(df["date_time"])

df=df.between_time(start_time="09:15:00",end_time="15:30:00",include_end=False)

df.dropna(inplace=True)
print(df)
df.to_csv("E:/sublime/intraday data/2014/Nifty/cleaned2014.csv",index=False)
# print(df.tail())

# df.columns=["ticker","date","time","open","high","low","close"]


# del df["ticker"]
# df.to_csv("E:/sublime/intraday data/Upto 2011/NIFTY upto 2011/2011nifty.csv",index=False)
# # print(df["date"])
# print(df.head())
