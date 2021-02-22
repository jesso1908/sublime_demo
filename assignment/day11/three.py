def pivot_values(O,H,L,C):
	pivot= (H+L+C)/3
	R1=2 *pivot -L
	R2=pivot+(H-L)
	R3=R1+(H-L)
	S1=2*pivot-H
	S2=pivot-(H-L)
	S3=S1-(H-L)
	return R3,R2,R1,pivot,S1,S2,S3	


previous_open=14789.05
previous_high=14913.7
previous_low=14714.5
previous_close=14895.65
pivot_list=[]
pivot_list=pivot_values(previous_open,previous_high,previous_low,previous_close)
print(pivot_list)