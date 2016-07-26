

import  time
import  pandas as pd
import  numpy as np
import  urllib2
import MySQLdb
import threadpool
import  threading
import  datetime
class WatchStock:
    def __init__(self):
        self.rowAll = []
        self.time_interval =300
        self.stockList =self.GetSqlData()
        self.url ='http://www.google.com/finance/getprices?i=60&p=1d&f=d,o,h,l,c,v&df=cpct&q='


    def GetData(self,symbol):
        path ='temp.txt'
        # fileContent = []
        # with  open(path,'r') as file:
        #     fileContent=file.readlines()
        #dt = pd.read_table('temp.txt')
        records = [line.replace(u'\n','').split(',') for line in urllib2.urlopen(self.url+symbol)]
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
        if max==df.iloc[-1,2]:
            self.rowAll.append(row_df)

    def GetSqlData(self):
        conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="root",db="finvizdb",charset="utf8")

        # read
        sql = "select No,Ticker,Price,Sector from spy500_tradestock "#limit 3,2
        df = pd.read_sql(sql,conn,index_col="No")
        df = df.dropna().iloc[:,0]
        print df.values
        return df.values

    def run(self,symbol):
        try:
           self.GetData(symbol)
        except Exception:
            print '111'

    def callback(request):
        pass
    def OverPrint(self):
        self.dfResult =  pd.DataFrame(self.rowAll,columns=['Ticker','Open','Close','Max','Min','FromOpen','FromMax','FromMin'])
        self.rowAll=[]
        print self.dfResult
    def start(self):
        print 'start-----------------------------'
        while True:
            time.sleep(self.time_interval)
            # thread_num = 100
            # pool = threadpool.ThreadPool(thread_num)
            # requests = threadpool.makeRequests(self.run(),['A'], self.callback())
            # [pool.putRequest(req) for req in requests]
            # pool.wait()
            # pool.dismissWorkers(thread_num, do_join=True)


            # threads=[]
            # for sy in self.stockList:
            #     threads.append(threading.Thread(target=self.run,args=(sy)))
            # for t in threads:
            #     t.setDaemon(True)
            #     t.start()
            for sy in self.stockList:
                self.run(sy)
            self.OverPrint()
            print 'Over====================================='+str(datetime.datetime.now())

    def test(self):
        threads=[]
        for sy in self.stockList:
            threads.append(threading.Thread(target=self.run,args=(sy)))
        for t in threads:
            t.setDaemon(True)
            t.start()
        #self.OverPrint(self)
watchStock = WatchStock()
watchStock.start()
#watchStock.GetSqlData()
#watchStock.test()