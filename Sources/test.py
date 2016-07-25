#encoding:utf-8
import  CommonMethod.myMethods as mm

import  json

import  numpy as np
import  pandas as pd

path ='temp.txt'

fileContent = open(path).readlines()
with  open("ttest.txt",'w') as file:
    file.write("111")
#dt = pd.read_table('temp.txt')

records = [line.replace(u'\n','').split(',') for line in open(path)]

dt = pd.DataFrame(records).dropna(how='any')

print dt
print records
