open_prices=[14458.5,14380.5,14581,14711.05,14593]
low_prices=[14250,14364.25,14524.1,14508.3,14356]
high_price=[14458.95,14586.3,14670.5,14765.45,14625.9]
close_prices=[14287.5,14570,14645.15,14598.6,14380.15]
avg_previousday=[]
for i,j in zip(open_prices,close_prices):
	avg_previousday.append((i+j)/2)
for i in range(len(close_prices)-1):
	if(open_prices[i]>close_prices[i]) and (open_prices[i+1]<low_prices[i]) and (close_prices[i+1]>high_price[i]):
		print("bullish engulfing")
	elif (open_prices[i]<close_prices[i]) and (open_prices[i+1]>=close_prices[i]) and (close_prices[i+1]<open_prices[i]):
		print("bearish engulfing")
	elif(high_price[i+1]<high_price[i]) and (low_prices[i+1]>low_prices[i]):
		print("inside bar")
	elif(open_prices[i]>close_prices[i]) and(open_prices[i+1]>close_prices[i]) and(close_prices[i+1]<open_prices[i]):
		print('bullish harami')
	elif(close_prices[i]>open_prices[i]) and (open_prices[i+1]<close_prices[i]) and (close_prices[i+1]>open_prices[i]):
		print("bearish harami")
	elif(close_prices[i]>open_prices[i]) and (open_prices[i+1]>high_price[i]) and (close_prices[i]<=avg_previousday[i]):
		print("dark cloud")
	elif(close_prices[i]<open_prices[i]) and(open_prices[i+1]<low_prices[i] and close_prices[i+1]>=avg_previousday[i]):
		print("Rising star")
	else:print("no pattern")
	
