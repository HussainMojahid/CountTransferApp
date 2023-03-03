from dbconfig import *
import time
import schedule

# schedule.every(1).seconds.do(dataPro.dataGet)
checkT=0
class dataPro:
    def dataGet():
        global checkT
        mydb._open_connection()
        mycurs=mydb.cursor()  
        mycurs.execute("select lcount from pcount ORDER BY id DESC LIMIT 1")
        checkT= mycurs.fetchone()
        tData=[]
        for i in checkT:
            # jk=(int(i)+1)
            # print(jk)
            tData.append(i)
        print(tData.pop())
        # tData.clear()
        mydb.close()

        
        # dataPro.run()
        
        return 
        

    def run():
        # if checkT == -20: 
        #     print("kuch to gadbad hai bhai.arram shea ")
        # else:
        dataPro.dataGet()

        # mycurs=mydb.cursor()  
        # mycurs.execute("select lcount from pcount ORDER BY id DESC LIMIT 1")
        # checkT= mycurs.fetchone()
        # tData=[]
        # for i in checkT:
            # jk=(int(i)+1)
            # print(jk)
            # tData.append(i)
        # print(tData.pop())
        # return dataGet
        

        # print("Hello new data",dataPro.dataGet)
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)
        return
schedule.every(5).seconds.do(dataPro.dataGet)
# mycurs=mydb.cursor()  
# mycurs.execute("select lcount from pcount ORDER BY id DESC LIMIT 1")
# checkT= mycurs.fetchone()
# tData=[]
# for i in checkT:
#     tData.append(i)
#     print(tData.pop())
    

while True:
    schedule.run_pending()
    time.sleep(1)