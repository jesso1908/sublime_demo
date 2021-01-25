last_Week_data=[[14458.5,14380.5,14581,14711.05,14593],[14250,14364.25,14524.1,14508.3,14356],
[4458.95,1458.3,14670.5,14765.45,14625.9],[14287.5,14570,14645.15,14598.6,14380.15],[13.2,11,8.85,9.92,16.4]]
print("open price",last_Week_data[0],"\nlow price",last_Week_data[1],
	"\nhigh price",last_Week_data[2],"\nclose price",last_Week_data[3],"\nvolume\t",last_Week_data[4])
total_volume=sum(last_Week_data[4])
print("total volume:",total_volume,"millions")
avg_close_price=sum(last_Week_data[3])/5
print("avg close price:",avg_close_price)
print("highest close price",max(last_Week_data[3]))
print("lowest close price:",min(last_Week_data[3]))
print("highest volume:",max(last_Week_data[4]),"millions")
print("lowest volume:",min(last_Week_data[4]),"millions")
