'''
Created on 2016年11月10日

@author: whyse
'''
from whyse.actionModel.util import StockBasicUtil
if __name__ == '__main__':
    '''
    二八轮动小市值+5,10,20均线金叉
    每天都需要跑，来寻找买入点
    '''
#     temp = StockBasicUtil.StockBasicUtil.getMyValuableStocks();
#     temp = StockBasicUtil.StockBasicUtil.getSmallValuableStocks();
    temp = StockBasicUtil.StockBasicUtil.getGroHighStocks(2000);
        
    pass