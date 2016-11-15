'''
Created on 2016年11月15日

@author: whyse
'''
import tushare as ts
if __name__ == '__main__':
    news = ts.get_latest_news(top=20)
    for item in news.iterrows():
        temp = item[1]
        print(temp['title']+' ： '+temp['url'])
    
    pass