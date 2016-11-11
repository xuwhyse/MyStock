'''
Created on 2016年11月7日

@author: whyse
'''
import datetime


class TimeUtil(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    @staticmethod
    def  getDateByType():
        """
        从所有股票中获取我认为值得投资的股票，比如不要st的
        """
        print(datetime.date.today()) #获取当前时间y-m-d
        
    @staticmethod
    def  getDateBOrA(d):
        """
        获取日期，前N天或者后N天
        """
        now = datetime.date.today()
        if d==0 :
            return str(now)
        else :
            return str(now+datetime.timedelta(d))
        
pass

