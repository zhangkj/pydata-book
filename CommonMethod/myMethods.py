#encoding:utf-8

import  os


#获取当前父路径
def GetParentPath():
    path = os.getcwd()
    parent_path = os.path.dirname(path)
    return parent_path+'\\'