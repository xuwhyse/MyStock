'''
Created on 2016年12月1日

@author: whyse
'''
from whyse.actionModel.util.WriteAndRead import WriteAndRead
from whyse.actionModel.util import StockBasicUtil
'''
筛选所有股票，只看均线金叉，突破+放量
属于断线题材，持股不超过一周，涨了就走，5%以上收益
'''
if __name__ == '__main__':
    path = 'F:\lianghua/bsStocksInfo'     #outstanding,流通股本(亿)  totals,总股本(亿)
    bsStocksInfo = WriteAndRead.readToFile(path)
    
    path = 'F:\lianghua/stocksTodayData'
    stocksTodayData = WriteAndRead.readToFile(path)
    stocksTodayData = stocksTodayData.set_index('code')
    
    for row in bsStocksInfo.iterrows():
        code = str(row[0])
        other = row[1]
        name = str(other[0])
        outstanding = other[4]
        totals = other[5]    #单位是亿
        if(totals>0):
            try:
                item = stocksTodayData.loc[code]
                trade = item['trade']  #现价
                ldzj = outstanding*trade #流动资金
                zzj = totals*trade  #总资金  50亿以内
                flag = StockBasicUtil.StockBasicUtil.isStockLineFine(code, 1.3)
                if(flag==1):
                    flag = StockBasicUtil.StockBasicUtil.isStockLinePW(code)
                    if(flag==1):
                        print(code+" "+name+"  "+str(ldzj)+"  "+str(zzj)+"   金叉，盘整突破+放量")
            except Exception as err:
                ()
    
    pass