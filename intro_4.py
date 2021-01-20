import nsepy as nse
from nsepy import get_history
import pandas as pd
from nsetools import Nse
from datetime import date
import matplotlib.pyplot as plt
nse= Nse()
adv_dec = nse.get_advances_declines()
print(adv_dec)
# df = pd.DataFrame(list(adv_dec.items()),columns = ['column1','column2'])
df=pd.DataFrame.from_dict(adv_dec)
# print(df)
vix = get_history(symbol="INDIAVIX",
            start=date(2015,1,1),
            end=date(2020,1,15),
            index=True)
print(vix["Close"].mean())
print(vix["Close"].min())
print(vix["Close"].max())
# plt.plot(vix["Close"].iloc[5:])
# plt.show()