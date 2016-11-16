'''
Created on 2016年11月16日

@author: whyse
'''
from whyse.actionModel.util.WriteAndRead import WriteAndRead
import tushare as ts

if __name__ == '__main__':
    
    #这边数据三个月跑一次就行
    
    # 主表市值那些
#     path = 'G:\lianghua/bsStocksInfo'
#     allSockets = ts.get_stock_basics()
#     WriteAndRead.writeToFile(path, allSockets)
    
    #成长数据，按照nprg,净利润增长率(%)排序保存的，这个比较好，因为经常超时
#     path = 'G:\lianghua/growthData'
#     data = ts.get_growth_data(2016,3)
#     WriteAndRead.writeToFile(path, data)
    
#     path = 'G:\lianghua/cashflowData'
#     data = ts.get_cashflow_data(2016,3)
#     WriteAndRead.writeToFile(path, data)
    
#     temp = WriteAndRead.readToFile(path)
#     print(temp)


    print("运行完毕！！！")
    pass