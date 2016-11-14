'''
Created on 2016年11月10日

@author: whyse
'''
import tushare as ts
import pandas as pd

# df = ts.get_sina_dd('300416', date='2016-11-11', vol=100) 
# print(df)

# allSockets = ts.get_stock_basics()
# df.to_csv('G:/lianghua/scBasics.csv',index_label='code')
# # df = ts.get_growth_data(2016,3).sort('nprg').head(100)
# df = pd.read_csv('G:\lianghua/scBasics.csv',encoding='gbk')
# index = df['code']
# columns=['code','name']
# ndf = df.reindex( index=index,columns=columns)
# item = df.loc['603977']
allSockets = ts.get_stock_basics()
item = allSockets.loc['300416']
print(item['totals'])
