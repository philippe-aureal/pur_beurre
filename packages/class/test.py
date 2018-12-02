import requests
import mysql.connector
from mysql.connector import errorcode
import json
from Api import *
from database import *
from pprint import pprint
import os

if __name__ == '__main__':
    test = Api()
    test.verif_files()
    bdd = Database()


    if test.verif== False:
        test.api_request()
        test.data_processing()
    try:
        bdd.connect()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            bdd.create_database()

    with open('../database/list.json','r') as f:
        datas = json.load(f)
    bdd.database_transfert(datas)
