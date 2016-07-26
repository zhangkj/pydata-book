#encoding:utf-8
import  CommonMethod.myMethods as mm

import  json

import  numpy as np
import  pandas as pd

rowAll = []
stockList =['A','AA']
for stock in stockList:
    print stock


for i in range(2):
    path ='temp.txt'
    # fileContent = []
    # with  open(path,'r') as file:
    #     fileContent=file.readlines()
    #dt = pd.read_table('temp.txt')
    records = [line.replace(u'\n','').split(',') for line in open(path)]
    nprecords = np.array(records[8:],dtype=np.float)

    df = pd.DataFrame(nprecords[:],columns=records[4]).dropna(how='any')
    des = df.describe()
    openP = df.iloc[0,4]
    close = df.iloc[-1,1]
    max = des.iloc[-1,2]
    min =des.iloc[3,-3]
    fromOpen =(close-openP)/openP*100
    fromMax = (close-max)/max*100
    fromMin = (close-min)/min*100
    avgVol = des.iloc[1,-1]
    max
    print des
    row_df =[openP,close,max,min,"%.2f%%" % fromOpen,"%.2f%%" % fromMax,"%.2f%%" % fromMin]
    print row_df
    rowAll.append(row_df)

print rowAll
dfAll = pd.DataFrame(rowAll,columns=['Open','Close','Max','Min','FromOpen','FromMax','FromMin'])
print dfAll

