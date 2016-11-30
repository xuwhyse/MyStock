'''
Created on 2016年11月9日

@author: whyse
'''
import tushare as ts
from whyse.actionModel.util.TimeUtil import TimeUtil

if __name__ == '__main__':
    
    sDate = TimeUtil.getDateBOrA(-30);
    eDate = TimeUtil.getDateBOrA(0);
    recentDays = 20;
    array = [recentDays]
    
    for i in array :
         
        fr = ts.get_hist_data('hs300',start=sDate,end=eDate,ktype='D')
        fr = fr.head(i)
        fr = fr.ix[:,'price_change'].sum()  #ix的操作
        print("沪深300 累计"+str(i)+"天涨幅："+str(fr))
         
        zz = ts.get_hist_data('399905',start=sDate,end=eDate,ktype='D')
        zz = zz.head(i)
        zz = zz.ix[:,'price_change'].sum()
        print("中证500 累计"+str(i)+"天涨幅："+str(zz))
        
        zxb = ts.get_hist_data('zxb')#获取中小板指数k线数据
        zxb = zxb.head(i)
        zxb = zxb.ix[:,'price_change'].sum()
        print("中小板 累计"+str(i)+"天涨幅："+str(zxb))
        
        cyb = ts.get_hist_data('cyb')#获取创业板指数k线数据
        cyb = cyb.head(i)
        cyb = cyb.ix[:,'price_change'].sum()
        print("创业板 累计"+str(i)+"天涨幅："+str(cyb))
    
    pass