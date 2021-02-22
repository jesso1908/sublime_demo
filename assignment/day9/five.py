Nifty_closing_price=[14238.90,14371.90,14590.35,14644.70,14521.15,14281.30,14433.70,14595.60,14564.85,14563.45,14484.75,
14347.25,14137.35,14146.25,14199.50,14132.90,14018.50]
SMA_5=[]
p=0
q=0
z=0
for i in range(len(Nifty_closing_price)):
	z=z+Nifty_closing_price[i]
	if i>4:
		q=z-sum(Nifty_closing_price[0:i-4])
		p=q/5
	SMA_5.append(p)
print(SMA_5)
sma_5=[0,0,0,0]
for i in range(4,len(Nifty_closing_price)):
	sum_price=Nifty_closing_price[i]+Nifty_closing_price[i-1]+Nifty_closing_price[i-2]+Nifty_closing_price[i-3]+Nifty_closing_price[i-4]
	avg=sum_price / 5
	sma_5.append(avg)
print("\n",sma_5)