with open('E:/sublime/intraday data/2014/Nifty/2014 JAN NIFTY.txt') as fp: 
    data = fp.read() 
with open('E:/sublime/intraday data/2015/Nifty/2015 FEB NIFTY.txt') as fp: 
    data1 = fp.read() 
with open('E:/sublime/intraday data/2015/Nifty/2015 MAR NIFTY.txt') as fp: 
    data2 = fp.read() 
with open('E:/sublime/intraday data/2015/Nifty/2015 APR NIFTY.txt') as fp: 
    data3 = fp.read() 
with open('E:/sublime/intraday data/2015/Nifty/2015 MAY NIFTY.txt') as fp: 
    data4 = fp.read() 
with open('E:/sublime/intraday data/2015/Nifty/2015 JUNE NIFTY.txt') as fp: 
    data5 = fp.read() 
# Reading data from file2 
with open('E:/sublime/intraday data/2015/Nifty/2015 JULY NIFTY.txt') as fp: 
    data6 = fp.read() 
with open('E:/sublime/intraday data/2015/Nifty/2015 AUG NIFTY.txt') as fp: 
    data7 = fp.read() 
with open('E:/sublime/intraday data/2015/Nifty/2015 SEP NIFTY.txt') as fp: 
    data8 = fp.read()
with open('E:/sublime/intraday data/2015/Nifty/2015 OCT NIFTY.txt') as fp: 
    data9 = fp.read()
with open('E:/sublime/intraday data/2015/Nifty/2015 NOV NIFTY.txt') as fp: 
    data10 = fp.read()
with open('E:/sublime/intraday data/2015/Nifty/2015 DEC NIFTY.txt') as fp: 
    data11 = fp.read() 
# Merging 2 files 
# To add the data of file2 
# from next line 
data += "\n"
data += data2 
data += data3
data += data4
data += data5
data += data6
data += data7
data += data8
data += data9
data += data10
data += data11

  
with open ('E:/sublime/intraday data/2015/Nifty/Combined.txt','w') as fp: 
    fp.write(data) 