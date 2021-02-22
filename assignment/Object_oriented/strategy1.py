import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/jesso/Desktop/TCS_1.csv")
# print(df)
print(df)
# print(close_price)
# true_range=[]
df["tr_1"]=abs(df["High"]-df["Low"])
df["tr_2"]=abs(df["High"]-df["Close"].shift())
df["tr_3"]=abs(df["Close"].shift()-df["Low"])
# print(df["tr_1"],df["tr_2"],df["tr_3"]))
compare=df.filter(items=["tr_1","tr_2",'tr_3'])
atr=compare.max(axis=1)
df['atr']=atr

print(df.columns)

df['atr_30'] = df.iloc[:,-1].rolling(window=30).mean()
print(df["atr_30"])

