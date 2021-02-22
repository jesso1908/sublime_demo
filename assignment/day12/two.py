low_prices=[14250,14364.25,14524.1,14508.3,14356]
high_price=[14458.95,14586.3,14670.5,14765.45,14625.9]
def price_range(high_price,low_prices):
	price_range=[]
	for i in range(len(high_price)):
		p_range=high_price[i]-low_prices[i]
		price_range.append(p_range)
	return price_range
a=price_range(high_price,low_prices)
print(a)