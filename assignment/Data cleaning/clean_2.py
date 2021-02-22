import pandas as pd 
df=pd.read_csv('E:/sublime/intraday data/2015/Nifty/Combined.txt',header=None)
# print(df)
df.columns=["ticker","date","time","open","high","low","close","extra"]
del df["ticker"]
del df["extra"]
print(df)

# import pandas as pd
# df_1=pd.read_csv("E:/sublime/intraday data/2013/Nifty/2013.csv")
# df=pd.read_csv("E:/sublime/intraday data/2013/Nifty/2013halfdata.csv")
# del df["extra"]
# # print(df_1)
# # print(df)
# df_2=pd.concat([df_1,df])
# print(df_2)
df.to_csv("E:/sublime/intraday data/2015/Nifty/uncleaned.csv",index=False)


