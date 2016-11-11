'''
Created on 2016年11月10日

@author: whyse
'''
import tushare as ts

temp = ts.get_hist_data('000613', start='2016-10-21',ktype='D').head(5)
# ix是最强的操作frame 能任意切割横向或者纵向，用起来奇怪点
temp = temp.ix[:,['ma5','ma10','ma20','turnover']]
print(temp.ix[0,'ma10']-temp.ix[0,'ma20'])

for row in temp.iterrows():
    aa = row[1]['ma10'] - row[1]['ma20']
    print(aa)