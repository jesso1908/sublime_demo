open_prices=[14458.5,14380.5,14581,14711.05,14593]
low_prices=[14250,14364.25,14524.1,14508.3,14356]
high_price=[14458.95,14586.3,14670.5,14765.45,14625.9]
close_prices=[14287.5,14570,14645.15,14598.6,14380.15]
volume=      [13.2,11,8.85,9.92,16.4]
turn_over=[]

# def turnover(high_price,low_prices,volume):
# 	for i in range(len(high_price)):
# 		turnover_value=((high_price[i]+low_prices[i])/2)*volume[i]
# 		turn_over.append(turnover_value)
# turnover(high_price,low_prices,volume)
# print(turn_over)

def turnover(high_price,low_prices,volume):
	turnover_list=[]
	for i in range(len(high_price)):
		turnover_value=((high_price[i]+low_prices[i])/2)* volume[i]
		turnover_list.append(turnover_value)
	return turnover_list
a=turnover(high_price,low_prices,volume)
print(a)