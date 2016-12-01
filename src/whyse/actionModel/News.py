'''
Created on 2016年11月15日

@author: whyse
'''
import tushare as ts
if __name__ == '__main__':
    
    guba = ts.guba_sina()
    print(guba)
    
    print("==============================================================")
    print("==============================================================")
    
    news = ts.get_latest_news(top=16)
    for item in news.iterrows():
        temp = item[1]
        print(temp['title']+' ： '+temp['url'])
    
    pass