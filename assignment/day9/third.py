volume= [13.2,11,8.85,9.92,16.4]
sum_0=0
for i in volume:
	sum_0=sum_0+i
print("the sum of voume is",sum_0,"millions")

for i in volume:
	avg=sum_0/len(volume)
print("the avg is",avg)
"""AVG CLOSING PRICE"""
close_prices=[14287.5,14570,14645.15,14598.6,14380.15]
for i in close_prices:
	avg_close=sum(close_prices)/len(close_prices)
print("the avg close price is",avg_close)
"""highest closing price"""
max_value=close_prices[0]
for i in close_prices:
	if i > max_value:
		max_value=i
print("the highest closing price is",max_value)
"""lowest closing price"""
min_value=close_prices[0]
for j in close_prices:
	if j<min_value:
		min_value=j
print("the lowest closing price is",min_value)

open_prices=[14458.5,14380.5,14581,14711.05,14593]
"""MAXIMUM OPENING PRICE"""
max_value=open_prices[0]
for i in open_prices:
	if i > max_value:
		max_value=i
print("the highest opening price",max_value)
"""MINIMUM OPENING PRICE"""
min_value=close_prices[0]
for j in close_prices:
	if j<min_value:
		min_value=j
print("the lowest closing price is",min_value)
"""HIGHEST HIGH PRICE"""
high_price=[14458.95,14586.3,14670.5,14765.45,14625.9]
max_value=high_price[0]
for i in high_price:
	if i > max_value:
		max_value=i
print("the highest high price",max_value)
"""LOWEST LOW PRICE"""
low_prices=[14250,14364.25,14524.1,14508.3,14356]
min_value=low_prices[0]
for j in low_prices:
	if j < min_value:
		min_value=j
print("the lowest low price",min_value)
price_range=[]
for i,j in zip(high_price,low_prices):
	price_range.append(i-j)
print(price_range)