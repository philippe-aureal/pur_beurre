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

    def data_verification(self, list_products):
        """method that checks and sorts the data
         before inserting into the database"""
        d = 0
        list_products_verified = copy.deepcopy(list_products)
        for dict in list_products:
            i = 0
            s = 0
            for item in dict:
                if ('nutrition_grade_fr' or 'brands' or 'product_name' or
                    'url' or 'stores') not in list_products[d][i]:
                    del list_products_verified[d][(i-s)]
                    s = s + 1
                i = i + 1
            d = d + 1
        return list_products_verified



    def database_transfert(self, list_products):
        """ method that transfers data to the database"""
        self.curA.execute("select count(*) from Product")
        nb=self.curA.fetchone()
        if nb[0] < 1:
            d = 0
            for dict in list_products:
                i = 0
                for item in dict:
                    self.curA.execute("INSERT INTO Product (name_product, brand_product, nutritional_note, url) VALUES (%s, %s, %s, %s)",
                                        (list_products[d][i]['product_name'], list_products[d][i]['brands'],
                                        list_products[d][i]['nutrition_grade_fr'], list_products[d][i]['url']))
                    cat=list_products[d][i]['categories']
                    store=list_products[d][i]['stores']
                    if cat == "plats-prepares-surgeles":
                        cat_id = 1
                        #self.curA.execute("INSERT IGNORE INTO Category (id, name_category) VALUES (%s, %s)", (cat_id, cat))
                        #self.curA.execute("insert INTO Product_Category (category_id) VALUES (%s)", (cat_id,))
                    elif cat == "boissons-aux-fruits":
                        cat_id = 2
                        #self.curA.execute("INSERT IGNORE INTO Category (id, name_category) VALUES (%s, %s)", (cat_id, cat))
                        #self.curA.execute("insert INTO Product_Category (category_id) VALUES (%s)", (cat_id,))
                    elif cat == "cereales-pour-petit-dejeuner":
                        cat_id = 3
                        #self.curA.execute("INSERT IGNORE INTO Category (id, name_category) VALUES (%s, %s)", (cat_id, cat))
                        #self.curA.execute("insert INTO Product_Category (category_id) VALUES (%s)", (cat_id,))
                    elif cat == "sandwichs":
                        cat_id = 4
                        #self.curA.execute("INSERT IGNORE INTO Category (id, name_category) VALUES (%s, %s)", (cat_id, cat))
                        #self.curA.execute("insert INTO Product_Category (category_id) VALUES (%s)", (cat_id,))
                    elif cat == "yaourts":
                        cat_id = 5
                        #self.curA.execute("INSERT IGNORE INTO Category (id, name_category) VALUES (%s, %s)", (cat_id, cat))
                        #self.curA.execute("insert INTO Product_Category (category_id) VALUES (%s)", (cat_id,))
                    self.curA.execute("INSERT IGNORE INTO Category (id, name_category) VALUES (%s, %s)", (cat_id, cat))

                    self.curA.execute("INSERT IGNORE INTO Store (id, name_store) VALUES (%s, %s)", (i, store))

                    #self.curA.execute("INSERT IGNORE INTO Store (name_store) VALUES(%s)",
                    #                    (list_products[d][i]['stores']))
                    i = i + 1
                d = d + 1
                self.bdd.commit()
