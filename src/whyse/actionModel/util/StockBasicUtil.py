'''
Created on 2016年11月7日

@author: whyse
'''
import tushare as ts
from whyse.actionModel.util.TimeUtil import TimeUtil
from whyse.actionModel.util.WriteAndRead import WriteAndRead

class StockBasicUtil(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    @staticmethod
    def  getMyValuableStocks(num):
        """
        从所有股票中获取我认为值得投资的股票，比如不要st的
        """
        df = WriteAndRead.readToFile('F:\lianghua/bsStocksInfo')
        df = df.sort("totalAssets").head(num)
        df = df.ix[:,['name']]
#         print(df)
        
        for row in df.iterrows():
#             row = row[1]  #这个调用小市值的时候需要这一步
            code = str(row[0])
            name = str(row[1])
            flag = 0
            try:
                flag = StockBasicUtil.isStockLineFine(code)
            except Exception:
    #             print(code+"有问题")
                flag = 0
            
            if (flag==1):
                print(name+'  '+code+"  可以买入")
        return df;
    
    @staticmethod
    def  getGroHighStocks(num):
        """
        获取成长率高的股票，并且均线选股
        """
        df = WriteAndRead.readToFile('F:\lianghua/growthData')
        allSocketsBase =WriteAndRead.readToFile('F:\lianghua/bsStocksInfo')
        path = 'F:\lianghua/stocksTodayData'
        stocksTodayData = WriteAndRead.readToFile(path)
        stocksTodayData = stocksTodayData.set_index('code')
        print('=======获取数据完毕，现在解析============')
        count = 0
        for row in df.iterrows():
            row = row[1]  #这个调用小市值的时候需要这一步
            code = str(row[0])
            name = str(row[1])
            nprg = row[3]
            count = count+1
            if(nprg<0):
                print('成长率即将为负数，运行了 ：'+str(count))
                return
            
            try:
                flag = 0
                item = allSocketsBase.loc[code]
                totals = item['totals']  #总股本
                outstanding =  item['outstanding']   #流通股本
                
                item = stocksTodayData.loc[code]
                trade = item['trade']  #现价
                ldzj = outstanding*trade #流动资金
                zzj = totals*trade  #总资金  50亿以内
                
                if(zzj<80 or ldzj<40):    #筛选总股本小宇4亿
                    flag=1
            except Exception :
                flag = 0
                
            if (flag==1):
                try:
                    flag = StockBasicUtil.isStockLineFine(code)
                except Exception :
                    flag = 0
                if (flag==1):
                    print(name+'  '+code+"  可以买关注")
                    flag = StockBasicUtil.isStockLinePW(code)
                    if (flag==1):
                        print(name+'  '+code+" 平稳！！ 可以买入")
           
        return df;
        
        
    #======================================================================
    #看来量比也要逐渐增大才能入围
    @staticmethod
    def isStockLineFine(sym,lbz=1.1):
        """
        lbz  当日量除以十日均量
        适合筛选出刚刚金叉的股票，筛选不出强势的股票
        1: 买入  0不是  -1 卖出
        判断这只股票是不是可以买入，或者应该卖出了。
        策略是十日均线上穿20日。  5日均线下传10日
        注意，如果监控已经买入的股票，这个函数每天要跑
        """
        sDate = TimeUtil.getDateBOrA(-8);
        temp = ts.get_hist_data(sym, start=sDate,ktype='D').head(4)
        # ix是最强的操作frame 能任意切割横向或者纵向，用起来奇怪点
        temp = temp.ix[:,['volume' ,'p_change' ,'ma5','ma10','ma20','turnover','v_ma10']]
        
        lb = temp.ix[0,'volume']/temp.ix[0,'v_ma10']  #当日量除以十日均量 >1.3比较好
        zf =  temp.ix[0,'p_change']     #涨幅这个参数需要
        
        by1 = temp.ix[0,'ma10']-temp.ix[0,'ma20']
        by2 = temp.ix[1,'ma10']-temp.ix[1,'ma20']
        by3 = temp.ix[2,'ma10']-temp.ix[2,'ma20']
        by4 = temp.ix[3,'ma10']-temp.ix[3,'ma20']
        
        sl1 = temp.ix[0,'ma10']-temp.ix[0,'ma5']
        sl2 = temp.ix[1,'ma10']-temp.ix[1,'ma5']
        sl3 = temp.ix[2,'ma10']-temp.ix[2,'ma5']
#         sl4 = temp.ix[3,'ma10']-temp.ix[3,'ma5']
        
        ma20CK = temp.ix[0,'ma20']/250
        ma21CK = ma20CK*1.2
#         34为负，1为正，或者1的数值很接近0就是买入点  sl1负代表5日均线上穿10日  and zf<4  and lb>1.2 
        if(by4 <0 and by3<0 and by2<0 and (by1>0 or abs(by1)<ma20CK) 
           and (abs(sl1)<ma21CK or sl1<0)  and lb>lbz ):
#             print('可以买入')
            return 1
        
        if(sl3<0 and sl2<0 and (sl1>0 or abs(sl1)<ma21CK)):
#             print('可以警告！！')
            return -1
            
        return 0;
    
    
    @staticmethod
    def isStockLineUp(sym):
        """
        筛选出当下处于上升趋势的股票
        5>10>20
        往后数两个月内取样的价格波动不大，再去除最近一周的20日均线的10%内
        """
        sDate = TimeUtil.getDateBOrA(-4);
        temp = ts.get_hist_data(sym, start=sDate,ktype='D').head(1)
        # ix是最强的操作frame 能任意切割横向或者纵向，用起来奇怪点
        temp = temp.ix[:,['volume' ,'p_change' ,'ma5','ma10','ma20','turnover','v_ma10']]
        
        lb = temp.ix[0,'volume']/temp.ix[0,'v_ma10']  #当日量除以十日均量 >1.3比较好
        zf =  temp.ix[0,'p_change']     #涨幅这个参数需要
        
        by1 = temp.ix[0,'ma10']-temp.ix[0,'ma20']
        sl1 = temp.ix[0,'ma10']-temp.ix[0,'ma5']
        flag = 0;
        if(by1>0 and sl1<0):
            flag =  1;
        if(flag==0):
            return 0;
        
        return StockBasicUtil.isStockLinePW(sym)
        return 0;
    
    
    @staticmethod
    def isStockLinePW(sym):
        """
        往后数两个月内取样的价格波动不大，再去除最近一周的20日均线的10%内
        返回1就是该线是平整，突破形态的
        """
        sDate = TimeUtil.getDateBOrA(-8);
        eDate = TimeUtil.getDateBOrA(-4);
        temp = ts.get_hist_data(sym, start=sDate,end=eDate,ktype='D').head(1)
        temp = temp.ix[:,['volume' ,'p_change' ,'ma5','ma10','ma20','turnover','v_ma10']]
        priceNow = temp.ix[0,'ma5']
        
        sDate = TimeUtil.getDateBOrA(-36);
        eDate = TimeUtil.getDateBOrA(-32);
        temp = ts.get_hist_data(sym, start=sDate,end=eDate,ktype='D').head(1)
        temp = temp.ix[:,['volume' ,'p_change' ,'ma5','ma10','ma20','turnover','v_ma10']]
        price1 = temp.ix[0,'ma5']
        priceCK = temp.ix[0,'ma20']*0.1
        
        if(abs(price1-priceNow)>priceCK):
            return 0;
        
        sDate = TimeUtil.getDateBOrA(-78);
        eDate = TimeUtil.getDateBOrA(-75);
        temp = ts.get_hist_data(sym, start=sDate,end=eDate,ktype='D').head(1)
        temp = temp.ix[:,['volume' ,'p_change' ,'ma5','ma10','ma20','turnover','v_ma10']]
        price2 = temp.ix[0,'ma5']
        
        if(abs(price1-price2)<priceCK  and abs(priceNow-price2)<priceCK*1.2):
            return 1;
            
        return 0;
    
    pass

# 对单只股票策略优化的调整
# aa = StockBasicUtil.isStockLineFine('000613')
# print(aa)
# StockBasicUtil.getMyValuableStocks()

# aa = StockBasicUtil.getSmallValuableStocks()
# print(aa)

# StockBasicUtil.getGroHighStocks(1500)



