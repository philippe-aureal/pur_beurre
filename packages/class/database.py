#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
from Api import *
from os import system
import copy


class Database():
    """class managing interactions with the database."""
    def __init__(self):
        """initalization of class"""
        #MySQLConfig = {'host':'192.168.1.77','user':'student',
                     #  'password':'wired', 'database':'pur_beurre'}
        #self.bdd = mysql.connector.connect(**MySQLConfig)
        #self.bdd = mysql.connector.connect(host="192.168.1.77",user="student",
        #                              password="wired")
        #self.cursor = self.bdd.cursor()

    def connect(self):
        """connection methode to the database"""
        self.bdd = mysql.connector.connect(host="192.168.1.77",user="student",
                                      password="wired", database="pur_beurre")

        self.curA = self.bdd.cursor()

    def create_database(self):
        self.bdd = mysql.connector.connect(host="192.168.1.77",user="student",
                                           password="wired")
        self.curA = self.bdd.cursor()
        for line in open('../database/create_database.sql').read().split(';\n'):
            self.curA.execute(line)


    def database_transfert(self, list_products):
        """ method that transfers data to the database"""
        self.curA.execute("select count(*) from Product")
        prod=self.curA.fetchone()
        self.curA.execute("select count(*) from Category")
        cat=self.curA.fetchone()
        self.curA.execute("select count(*) from Store")
        store=self.curA.fetchone()

        if len(prod) < 1 or len(cat) < 5 or len(store) < 1:
            i=1
            for item in list_products:
                self.curA.execute("INSERT IGNORE INTO Category (name_category) VALUES (%s)", (item['categories'],))
                self.curA.execute("select id from Category where name_category = %s", (item['categories'],))
                cat_id = self.curA.fetchone()
                self.curA.execute("INSERT IGNORE INTO Store (name_store) VALUES (%s)", (item['stores'],))
                self.curA.execute("select id from Store where name_store = %s", (item['stores'],))
                store_id = self.curA.fetchone()
                self.curA.execute("INSERT INTO Product (name_product, brand_product, nutritional_note, url, category_id) VALUES (%s, %s, %s, %s, %s)",
                                    (item['product_name'], item['brands'],
                                    item['nutrition_grade_fr'], item['url'], cat_id[0]))
                #self.curA.execute("select id from Product where name_product = %s", (item['product_name'],))
                #prod_id = self.curA.fetchone()
                #print(prod_id)
                self.curA.execute("INSERT INTO Product_Store (store_product_id, store_id) VALUES (%s, %s)", (i, store_id[0]))
                i=i+1
                #self.curA.execute("INSERT IGNORE INTO Product (category_id) VALUES (%s)", cat_id[0])

            self.bdd.commit()
