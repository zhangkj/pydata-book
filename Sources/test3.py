#encoding:utf-8

#=========map并行检测数据


import time,random
import  pandas as pd
import  numpy as np
import  urllib2
import MySQLdb
import threadpool
import  threading
import  datetime
import urllib2
from multiprocessing.dummy import Pool as ThreadPool

def __init__(self):
    self.rowAll = []
    self.time_interval =300
    self.stockList =self.GetSqlData()


def GetData(symbol):
    path ='temp.txt'
    # fileContent = []
    # with  open(path,'r') as file:
    #     fileContent=file.readlines()
    #dt = pd.read_table('temp.txt')
    url ='http://www.google.com/finance/getprices?i=60&p=1d&f=d,o,h,l,c,v&df=cpct&q='
    #records = [line.replace(u'\n','').split(',') for line in open(path)]
    records = [line.replace(u'\n','').split(',') for line in urllib2.urlopen(url+symbol)]
    nprecords = np.array(records[8:],dtype=np.float)

    df = pd.DataFrame(nprecords[:],columns=records[4]).dropna(how='any')

    #print df
    des = df.describe()
    openP = df.iloc[0,4]
    close = df.iloc[-1,1]
    max = des.iloc[-1,2]
    min =des.iloc[3,-3]
    fromOpen =(close-openP)/openP*100
    fromMax = (close-max)/max*100
    fromMin = (close-min)/min*100
    avgVol = des.iloc[1,-1]
    ticker = symbol
    #openP,close,max,min,"%.2f%%" % fromOpen,"%.2f%%" % fromMax,"%.2f%%" % fromMin
    row_df =[ticker,openP,close,max,min,fromOpen,fromMax,fromMin]
    return  row_df
    # if max==df.iloc[-1,2]:
    #     return row_df

def GetSqlData():
    conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="root",db="finvizdb",charset="utf8")

    # read
    sql = "select No,Ticker,Price,Sector from spy500_tradestock "#limit 3,2  spy500_tradestock
    df = pd.read_sql(sql,conn,index_col="No")
    df = df.dropna().iloc[:,0]
    print df.values
    return df.values
def run(symbol):
    try:
        return GetData(symbol)
    except Exception:
        print symbol+' is error'
if __name__ == '__main__':
    starttime = datetime.datetime.now()
    stockList = GetSqlData()
    # Make the Pool of workers
    pool = ThreadPool(500)
    # Open the urls in their own threads
    # and return the results
    results = pool.map(run, stockList)
    #close the pool and wait for the work to finish
    pool.close()
    pool.join()
    dfResult =  pd.DataFrame(results,columns=['Ticker','Open','Close','Max','Min','FromOpen','FromMax','FromMin'])
    print dfResult

    endtime= datetime.datetime.now()
    print (endtime-starttime).seconds