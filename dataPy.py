from dbconfig import *
import time
import schedule






#----postgresql--connection-------------------------------------------

# print(mydb)
# mycurs=mydb.cursor()  
# mycurs.execute("Select * FROM pcount")
#     # global myresult
# myresult = mycurs.fetchone()
# print(myresult)

# mycurs=mydb.cursor()  
# mycurs.execute("select lcount from pcount ORDER BY id DESC LIMIT 1")
# myresult = mycurs.fetchone()
# print(myresult)

#------Function--Start--------------------------------------------------

def secdule_count():
    # global myresult
    #recent comment
    mydb._open_connection()
    mycurs=mydb.cursor()  
    mycurs.execute("select lcount from pcount ORDER BY id DESC LIMIT 1")

    # mycurs.execute("select * from lcount ORDER BY id DESC LIMIT 1")
    
    # print(mycurs.execute)

    # print(mycurs.fetchone())

    #recent comment
    myresult = mycurs.fetchone()
    # print(mycurs.fetchone())

    # return myresult
    mydb.close()
#--------------------------------------------------------------------    
    global resData
    for i in myresult:
        resData=i
# -------------------------------------------    
    # print(resData)
    # print(resData)
#--------------------------------
def posdata_insert():
    # print(resData)
    poscursor=conn.cursor()
    posql = poscursor.execute("UPDATE peopler_counts SET rcounting = (%s) WHERE id = 1"%(resData))
    # posql = poscursor.execute("INSERT INTO peopler_counts(rcounting) VALUES (%s)"%(resData))
    conn.commit()

#-------------------------------
# print(resData)
schedule.every(1).seconds.do(secdule_count)
schedule.every(7).seconds.do(posdata_insert)


while True:
    schedule.run_pending()
    time.sleep(1)

# print(secdule_count())
# print(posdata_insert())
