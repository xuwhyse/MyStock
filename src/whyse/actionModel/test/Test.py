'''
Created on 2016年11月10日

@author: whyse
'''
import tushare as ts
import pandas as pd
from whyse.actionModel.util.WriteAndRead import WriteAndRead

# df = ts.get_sina_dd('300416', date='2016-11-11', vol=100) 
# print(df)
path = 'G:\lianghua/bsStocksInfo'

allSockets = ts.get_stock_basics()
WriteAndRead.writeToFile(path, allSockets)

temp = WriteAndRead.readToFile(path)
print(temp)
# allSockets.to_json('G:\lianghua/scBasics.json',orient='records')
# df.to_csv('G:/lianghua/scBasics.csv',index_label='code')
# # df = ts.get_growth_data(2016,3).sort('nprg').head(100)
# df = pd.read_csv('G:\lianghua/scBasics.csv',encoding='gbk')
# index = df['code']
# columns=['code','name']
# ndf = df.reindex( index=index,columns=columns)
# item = df.loc['603977']

# allSockets = ts.get_stock_basics()
# item = allSockets.loc['300416']
# print(item['totals'])
