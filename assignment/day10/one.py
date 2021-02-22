open_prices=[14458.5,14380.5,14581,14711.05,14593]
low_prices=[14250,14364.25,14524.1,14508.3,14356]
high_price=[14458.95,14586.3,14670.5,14765.45,14625.9]
close_prices=[14287.5,14570,14645.15,14598.6,14380.15]
volume=      [13.2,11,8.85,9.92,16.4]
# turnover=[]
# zip_object=zip(high_price,low_prices,volume)
# for i,j,z in zip_object:
# 	turnover.append(((i+j)/2)*z)
i=0
while i<len(open_prices):
	print("open prices:",open_prices[i])
	i=i+1

j=0
while j<len(low_prices):
	print("low prices",low_prices[j])
	j=j+1
k=0
while k<len(high_price):
	print("highprices",high_price[k])
	k=k+1
l=0
while l<len(close_prices):
	print("close prices",close_prices[l])
	l=l+1
m=0
while m<len(volume):
	print("volume",volume[m])
	m=m+1