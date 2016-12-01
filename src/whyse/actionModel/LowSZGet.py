'''
Created on 2016年12月1日

@author: whyse
'''
from whyse.actionModel.util.WriteAndRead import WriteAndRead
from whyse.actionModel.util import StockBasicUtil

if __name__ == '__main__':
    path = 'F:\lianghua/bsStocksInfo'     #outstanding,流通股本(亿)  totals,总股本(亿)
    bsStocksInfo = WriteAndRead.readToFile(path)
    
    path = 'F:\lianghua/stocksTodayData'
    stocksTodayData = WriteAndRead.readToFile(path)
    stocksTodayData = stocksTodayData.set_index('code')
    
    growthData = WriteAndRead.readToFile('F:\lianghua/growthData')
    growthData = growthData.set_index('code')

    bsStocksInfo = bsStocksInfo.sort("totals").head(2500);
    
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
                if((zzj<60 or ldzj<30)and zzj!=0):
                    flag = StockBasicUtil.StockBasicUtil.isStockLineUp(code)
                    if(flag==1):
#                         print(code+" "+name+"  "+str(ldzj)+"  "+str(zzj))
                        #======增加净利润增长率大于0==============
                        item = growthData.loc[code]
                        nprg = item['nprg']  #净利润增长率(%)
                        if(nprg>0):
                            print(code+" "+name+"  "+str(ldzj)+"  "+str(zzj))
                        #===================================
            except Exception as err:
                ()
    
    pass