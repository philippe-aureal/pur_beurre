import requests
import mysql.connector
import json
from Api import *
from database import *
from pprint import pprint
import os

if __name__ == '__main__':
    test = Api()
    test.verif_files()

    if test.verif== True:

        test.data_processing()





    """with open('dict2.json','r') as f:
        datas = json.load(f)
    pprint(datas[0])"""



"""    try:
    bdd.connect()
    bdd.create_database()
    list = []
    list = bdd.data_verification(test.list_products)
    i =0
    for item in list:
        print(list[i][14]['categories'])
        i = i+1
    bdd.database_transfert(list)"""
#with open('../database/list.json','w') as f:
