Nifty_closeprice=[14895.65,14789.95,14647.85,13634.6,13817.55,13967.5,14238.9,14371.9,14590.35,14644.7,14521.15,14281.3,
14433.7,14595.6,14564.85,14563.45,14484.75,14347.25,14137.35,14146.25,14199.5]
Nifty_closeprice.reverse()
def simple_average(Nifty_closeprice):
	sma_5=[0,0,0,0]

	for i in range(4,len(Nifty_closeprice)):
			sma_value= (Nifty_closeprice[i]+Nifty_closeprice[i-1]+Nifty_closeprice[i-2]+Nifty_closeprice[i-3]+Nifty_closeprice[i-4])/5
			sma_5.append(sma_value)
	return sma_5
a=simple_average(Nifty_closeprice)
print(a)

