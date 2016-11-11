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
    temp = StockBasicUtil.StockBasicUtil.getSmallValuableStocks();
    for row in temp.iterrows():
        row = row[1]  #这个调用小市值的时候需要这一步
        code = str(row[0])
        name = str(row[1])
        flag = 0
        try:
            flag = StockBasicUtil.StockBasicUtil.isStockLineFine(code)
        except Exception as err:
#             print(code+"有问题")
            flag = 0
        
        if (flag==1):
            print(name+'  '+code+"  可以买入")
        
    pass