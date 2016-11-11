'''
Created on 2016年11月7日

@author: whyse
'''
import tushare as ts
from whyse.actionModel.util.TimeUtil import TimeUtil

class StockBasicUtil(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    @staticmethod
    def  getMyValuableStocks():
        """
        从所有股票中获取我认为值得投资的股票，比如不要st的
        """
        count = 2800
        df = ts.get_stock_basics()
        df = df.sort("totalAssets").head(count)
        df = df.ix[:,['name']]
#         print(df)
        return df;
    
    @staticmethod
    def  getSmallValuableStocks():
        """
        选取中小股票样本
        总股本不大于3亿，流通股本不大于2亿。总股本在1.5亿到2亿之间最佳
        总市值在30亿左右，流通市值在20亿左右
        前十大股东占股本50%以上，越大越好。如果能有在70%以上的，而股价没怎么涨
        """
        df = ts.get_sme_classified()
#         df = df.sort("totalAssets").head(count)
#         df = df.ix[:,['name']]
#         print(df)
        return df;
        
    @staticmethod
    def isStockLineFine(sym):
        """
        适合筛选出刚刚金叉的股票，筛选不出强势的股票
        1: 买入  0不是  -1 卖出
        判断这只股票是不是可以买入，或者应该卖出了。
        策略是十日均线上穿20日。  5日均线下传10日
        注意，如果监控已经买入的股票，这个函数每天要跑
        """
        sDate = TimeUtil.getDateBOrA(-10);
        temp = ts.get_hist_data(sym, start=sDate,ktype='D').head(4)
        # ix是最强的操作frame 能任意切割横向或者纵向，用起来奇怪点
        temp = temp.ix[:,['ma5','ma10','ma20','turnover']]
        
        by1 = temp.ix[0,'ma10']-temp.ix[0,'ma20']
        by2 = temp.ix[1,'ma10']-temp.ix[1,'ma20']
        by3 = temp.ix[2,'ma10']-temp.ix[2,'ma20']
        by4 = temp.ix[3,'ma10']-temp.ix[3,'ma20']
        
        sl1 = temp.ix[0,'ma10']-temp.ix[0,'ma5']
        sl2 = temp.ix[1,'ma10']-temp.ix[1,'ma5']
        sl3 = temp.ix[2,'ma10']-temp.ix[2,'ma5']
        sl4 = temp.ix[3,'ma10']-temp.ix[3,'ma5']
        
#         print(temp)
#         
#         print('by1：'+str(by1))
#         print('by2：'+str(by2))
#         print('by3：'+str(by3))
#         print('by4：'+str(by4))
#          
#         print('sl1：'+str(sl1))
#         print('sl2：'+str(sl2))
#         print('sl3：'+str(sl3))
#         print('sl4：'+str(sl4))
        
        ma20CK = temp.ix[0,'ma20']/250
        ma21CK = ma20CK*1.2
#         34为负，1为正，或者1的数值很接近0就是买入点  sl1负代表5日均线上穿10日
        if(by3<0 and by2<0 and (by1>0 or abs(by1)<ma20CK) and (abs(sl1)<ma21CK or sl1<0)):
#             print('可以买入')
            return 1
        
        if(sl3<0 and sl2<0 and (sl1>0 or abs(sl1)<ma21CK)):
#             print('可以警告！！')
            return -1
            
        return 0;
    pass

# 对单只股票策略优化的调整
# aa = StockBasicUtil.isStockLineFine('000613')
# print(aa)
# StockBasicUtil.getMyValuableStocks()

# aa = StockBasicUtil.getSmallValuableStocks()
# print(aa)



