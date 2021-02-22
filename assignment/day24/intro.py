from __future__ import (  absolute_import,division,print_function,unicode_literals)
import backtrader as bt
from datetime import datetime
import pandas as pd 
class Firststrategy(bt.Strategy):
	params=(("exitbars",3),)
	def __init__(self):
		self.dataclose=self.datas[0].close
		self.datetime=self.datas[0].datetime ## proprietary backtader line buffer
		self.candletracker=0
	def log(self,txt):
		# dt= dt or self.datas[0].datetime(0)

		# print(pd.datetime(dt).isoformat())
		print(txt)
	def next(self):
		# print("close :",self.dataclose[0])
		# self.log(str(self.datetime[0]) +str(self.dataclose[0]))
		self.log(str(self.dataclose[0]))
		if not self.position:
			if self.dataclose[0]> self.dataclose[-1]:
				if self.dataclose[-1] > self.dataclose[-2]:
					self.order=self.buy()
					self.log("buy : "+ str(self.dataclose[0]))	
					self.candletracker=0
		else:
			self.candletracker += 1
			print(self.params.exitbars)
			if self.candletracker > self.params.exitbars:
				self.close()
				self.log("sell : " + str(self.dataclose[0]))
				self.candletracker=0





if __name__== "__main__":

	cerebro=bt.Cerebro()
	cerebro.addstrategy(Firststrategy,exitbars=5)
	# datapath="C:/Users/jesso/Desktop/TCS_1.csv"
	datapath="E:/sublime/assignment/Data cleaning/Nifty-1D.csv"
	data=bt.feeds.GenericCSVData(
		dataname=datapath,
		fromdate=datetime(2011,1,1),
		todate=datetime(2018,1,1),
	    datetime=0,
	    timeframe=bt.TimeFrame.Days,
	    compression=1,
	    dtformat=("%Y-%m-%d"),
	    open=1,
	    high=2,
	    low=3,
	    close=4,
	    volume=None,openinterest=None,reverse=False,header=0)
	cerebro.adddata(data)
	cerebro.broker.setcash(1000000.00 )
	cerebro.broker.setcommission(commission=0.001)
	cerebro.addsizer(bt.sizers.FixedSize,stake=75)





	print("Starting portfolio value :",cerebro.broker.getvalue())
	cerebro.run()
	print("Final portfolio value :",cerebro.broker.getvalue())