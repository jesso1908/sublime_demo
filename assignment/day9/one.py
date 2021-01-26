open_prices=[14458.5,14380.5,14581,14711.05,14593]
low_prices=[14250,14364.25,14524.1,14508.3,14356]
high_price=[14458.95,14586.3,14670.5,14765.45,14625.9]
close_prices=[14287.5,14570,14645.15,14598.6,14380.15]
volume=      [13.2,11,8.85,9.92,16.4]
turnover=[]
zip_object=zip(high_price,low_prices,volume)
for i,j,z in zip_object:
	turnover.append(((i+j)/2)*z)
# print(turnover)
# for i in open_prices:
# 	print(i)
# for i in low_prices:
# 	print(i)
# for i in high_price:
# 	print(i)
# for i in close_prices:
# 	print(i)
# for i in volume:
# 	print(i)
# for i in turnover:
# 	print(i)
for i in range(5):
	print("Open price:",open_prices[i],"low prices:",low_prices[i],"High prices",high_price[i],"close_prices:",close_prices[i],"volume:",volume[i],"turnover",turnover)