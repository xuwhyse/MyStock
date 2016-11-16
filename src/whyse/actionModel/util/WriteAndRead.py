'''
Created on 2016年11月16日

@author: whyse
'''
import pickle
class WriteAndRead(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
    @staticmethod
    def  writeToFile(path,data):
        """
         把data序列化到指定地址,二进制文件
         'G:\lianghua/test'
        """
        temp = pickle.dumps(data);
        output = open(path,'wb')
        output.write(temp)
        output.close()
        
    @staticmethod
    def  readToFile(path):
        '''
        将二进制文件反序列化到对象
        '''
        input = open(path,'rb')
        temp = input.read();
        input.close();
        return pickle.loads(temp);
    #===================================================
    
    