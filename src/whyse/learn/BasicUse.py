
import tushare as ts

temp = ts.get_hist_data('300134', start='2016-09-01',ktype='W')
print(temp)

# temp = ts.get_realtime_quotes('300033')
# print(temp)

#获取大盘数据
# print(ts.get_index())

# 大单数据
#print( ts.get_sina_dd('300033', date='2016-11-04', vol=200) )

# 获取概念最近的分红信息
# df = ts.profit_data(year=2016,top=30)
# df.sort('shares',ascending=False)
# print(df)
