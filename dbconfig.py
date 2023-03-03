import mysql.connector
import psycopg2
from jproperties import Properties


configs = Properties()
with open('dbcred.properties', 'rb') as read_prop:
    configs.load(read_prop)

prop_view = configs.items()
# print(type(prop_view))
# for item in prop_view:
#     print(item)

dbname=(configs.get("PDB_database").data)
print(dbname)

dbuser=(configs.get("PDB_user").data)
print(dbuser)
dbpassword=(configs.get("PDB_password").data)
dbhost=(configs.get("PDB_host").data)
# dbport=(configs.get("PDB_port").data)

# conn = psycopg2.connect(database=(configs.get("PDB_database").data),user=(configs.get("PDB_user").data),password=(configs.get("PDB_password").data),host=(configs.get("PDB_host").data),port=(configs.get("PDB_port").data))
conn = mysql.connector.connect(
  host=(configs.get("PDB_host").data),
  user=(configs.get("PDB_user").data),
  password=(configs.get("PDB_password").data),
  database=(configs.get("PDB_database").data)

)

print(conn)
#------------------Mysql--connection----------------------------------
mydb = mysql.connector.connect(
  host=(configs.get("MDB_host").data),
  user=(configs.get("MDB_user").data),
  password=(configs.get("MDB_password").data),
  database=(configs.get("MDB_database").data)

)

print(mydb)