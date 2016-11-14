'''
Created on 2016年11月11日

@author: whyse
'''
from whyse.actionModel.util import StockBasicUtil

if __name__ == '__main__':
    listCode = ['300416','300231']  #这里面是需要监控的股票池
    for code in listCode:
        flag = 0
        try:
            flag = StockBasicUtil.StockBasicUtil.isStockLineFine(code)
        except Exception as err:
#             print(code+"有问题")
            flag = 0
        
        if (flag==-1):
            print(code+"警告！！！")
        else:
            print(code+"：fine")
    print('本次监控买入的股票执行完毕')
    pass