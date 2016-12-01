'''
Created on 2016年11月16日

@author: whyse
'''
from whyse.actionModel.util.WriteAndRead import WriteAndRead
import tushare as ts

if __name__ == '__main__':
    
    #这边数据三个月跑一次就行
    
    '''
    code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数
    '''
    # 主表市值那些
#     path = 'F:\lianghua/bsStocksInfo'
#     allSockets = ts.get_stock_basics()
#     WriteAndRead.writeToFile(path, allSockets)
     
    '''
     code,代码
name,名称
mbrg,主营业务收入增长率(%)
nprg,净利润增长率(%)
nav,净资产增长率
targ,总资产增长率
epsg,每股收益增长率
seg,股东权益增长率
    '''
    #成长数据，按照nprg,净利润增长率(%)排序保存的，这个比较好，因为经常超时
    path = 'F:\lianghua/growthData'
    data = ts.get_growth_data(2016,3)
    WriteAndRead.writeToFile(path, data)
     
    
#     path = 'F:\lianghua/cashflowData'
#     data = ts.get_cashflow_data(2016,3)
#     WriteAndRead.writeToFile(path, data)
    
    '''
    code：代码
name:名称
changepercent:涨跌幅
trade:现价
open:开盘价
high:最高价
low:最低价
settlement:昨日收盘价
volume:成交量
turnoverratio:换手率
    '''
#         当日价格，计算总市值和流动市值    trade
#     path = 'F:\lianghua/stocksTodayData'
#     data = ts.get_today_all()
#     WriteAndRead.writeToFile(path, data)
    
#     temp = WriteAndRead.readToFile(path)
#     print(temp)

    print("运行完毕！！！")
    pass