yesterday=[14754.9,14868.85,14574.15,14789.95]
today=[14789.05,14913.7,14714.5,14895.65]
def is_insidebar(yesterday,today):
	if(today[1]<yesterday[1]) and (today[2]>yesterday[2]):
		return True
def is_bullishengulfing(yesterday,today):
	if(yesterday[3]<yesterday[0]) and (yesterday[1]<today[1]) and (yesterday[3]>today[3]):
		return True
def is_bearishengulfing(yesterday,today):
	if(yesterday[3]>yesterday[0]) and (yesterday[1]<today[1]) and (yesterday[3]>today[3]):
		return True
def is_bullishharami(yesterday,today):
	if(yesterday[0]>yesterday[3]) and (today[1]<yesterday[0]) and (today[2]>yesterday[3]):
		return True
def is_bearishharami(yesterday,today):
	if(yesterday[0]<yesterday[3]) and (today[1]<yesterday[3]) and (today[2]>yesterday[0]):
		return True





a=is_insidebar(yesterday,today)
if a:
	print("inside bar")
else:
	print("Does not fulfill inside bar")

b=is_bullishengulfing(yesterday,today)
if b:
	print("Bullish engulfing")
else:
	print("Does not fulfill bullish engulfing")
c=is_bearishengulfing(yesterday,today)
if c:
	print("bearish engulfing pattern")
else:
	print("Does not fulfill bearish engulfing")
d=is_bullishharami(yesterday,today)
if d:
	print("Bullish harami pattern")
else:
	print("Does not fulfill bullish harami pattern")
e=is_bearishharami(yesterday,today)
if e:
	print("Bearish harami pattern")
else:
	print("does not fulfill bearish harami pattern")