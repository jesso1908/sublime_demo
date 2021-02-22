open_prices=[14458.5,14380.5,14581,14711.05,14593]
low_prices=[14250,14364.25,14524.1,14508.3,14356]
high_price=[14458.95,14586.3,14670.5,14765.45,14625.9]
close_prices=[14287.5,14570,14645.15,14598.6,14380.15]
"""BULLISH ENGULFING

if(previous_open>previous_close) and (current_open<previous_low and current_close>previous_high)"""
if(open_prices[0]>close_prices[0]) and (open_prices[1]<low_prices[0]) and (close_prices[1]>high_price[0]):
	print("bullish engulfing")
	"""BEARISH ENGULFING"
	previous_open<previous_close) and (current_open>=previous_close and current_close<previous_open) """
elif(open_prices[0]<close_prices[0]) and (open_prices[1]>=close_prices[0]) and (close_prices[1]<open_prices[0]):
	print("bearish engulfing")
	"""INSIDE BAR
	(current_high<previous_high) and (current_low>previous_low)"""
elif(high_price[1]<high_price[0]) and (low_prices[1]>low_prices[0]):
	print("inside bar")
else:
	print("no pattern visible")
