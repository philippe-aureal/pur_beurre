import requests
import mysql.connector
from mysql.connector import errorcode
import json
from Api import *
from database import *




bdd = mysql.connector.connect(host="192.168.1.77",user="student",
                                       password="wired")
curA = bdd.cursor()
for line in open('../database/create_database.sql').read().split(';\n'):
    #print(line)
    curA.execute(line)
"""if __name__ == '__main__':
    test = Api()
    test.request_api()
    #print(test.list_products[0][14]['product_name'])
    bdd = Database()
    #bdd.connect()
  try:
        bdd.connect()
        #print(type(bdd.bdd))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            bdd.create_database()"""
    #print(bdd.get_row)


#list = []
#list = bdd.data_verification(test.list_products)
#i =0
#for item in list:
#print(list[i][14]['categories'])
#i = i+1
#bdd.database_transfert(list)
#bdd.curA.execute("""select count(id) from Product""")
#name=bdd.curA.fetchone()
#print(name[0])
