from  __future__ import(absolute_import,division,print_function,unicode_literals)
import backtrader as bt 
from datetime import datetime
class Secondstrategy(bt.Strategy):
	def log(self,txt):
		print(txt)
	def __init__(self):
		self.dataclose=self.datas[0].close
		self.candletracker=0



	def next(self):
		self.log("Close"+ str(self.dataclose[0]))
		if not self.position:
			if self.dataclose[0]>self.dataclose[-1]:
				if self.dataclose[-1]>self.dataclose[-2]:
					self.order=self.buy()
					self.log("Buy Order :"+str(self.dataclose[0]))
					self.candletracker=0
		else:
			self.candletracker += 1
			if self.candletracker > 4:
				self.close()
				self.log("order exited :"+str(self.dataclose[0]))



if __name__=="__main__":
	cerebro=bt.Cerebro()
	cerebro.addstrategy(Secondstrategy)
	datapath="E:/sublime/intraday data/cleaned nifty/cleaned2011.csv"
	
	data=bt.feeds.GenericCSVData(
		dataname=datapath,
		fromdate=datetime(2008,1,1,9,55),
		todate=datetime(2011,12,29,15,29),
		datetime=0,
		timeframe=bt.TimeFrame.Minutes,
		compression=1,
	    dtformat=("%Y-%m-%d %H:%M:%S"),
	    open=1,
	    high=2,
	    low=3, 
	    close=4,
	    openinterest=-1,
	    volume=-1,
		reverse=False,header=0,
		
		)
	cerebro.adddata(data)
	cerebro.broker.setcash(1000000.00)

	print("Starting portfolio value :",cerebro.broker.getvalue())
	cerebro.run()
	print("Final portfolio value :",cerebro.broker.getvalue())