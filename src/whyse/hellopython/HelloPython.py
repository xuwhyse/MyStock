#!/usr/bin/python
#coding: UTF-8 
#"#"号是注释
"""
这个是多行注释
sdgfdh
sdg
"""
name = "hello world";
print (name);
print  (name[2:5]);
print("你好,徐岷");
#==========================================
a = 6;
b = 5;
if(a>b):
    print("A大")
else:
    print("B大")
#==========================================
strTemp = "你好"
strTemp +=a.__str__();
print (strTemp);


import tushare
print(tushare.__version__)