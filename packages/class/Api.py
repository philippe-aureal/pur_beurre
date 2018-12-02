#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import os
import copy

class Api:
    """class used to build api requests"""
    def __init__(self):

        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.querystring = {"action":"process","tagtype_0":"categories",
                            "tag_contains_0":"contains",
                            "tag_0":"",
                            "page_size":"500","sort_by":"unique_scans_n",
                            "json":"1"}
        self.headers = {
            'cache-control': "no-cache",
            'Postman-Token': "354050b8-d327-4d4c-aebf-4737341ac849"
            }
        self.category = ("plats-prepares-surgeles","boissons-aux-fruits",
                         "cereales-pour-petit-dejeuner", "sandwichs", "yaourts")
        self.list_products = []
        self.dict ={}
        self.products = {}


    def api_request(self):
        """ create the request according to the category requested"""

        for item in self.category:
            self.querystring['tag_0'] = item
            response = requests.request("GET", self.url, headers=self.headers,
                                        params=self.querystring)
            self.dict = response.json()
            self.products = self.dict["products"]
            i = 0
            for element in self.products:
                self.products[i]['categories'] = item
                self.list_products.append(self.products[i])
                i=i+1

    def data_processing(self):

        self.products_verified = copy.deepcopy(self.list_products)
        s = 0
        i = 0
        for dictio in self.list_products:
            if ('nutrition_grade_fr' or 'brands' or 'product_name' or
                'url' or 'stores') not in self.list_products[i]:
                del self.products_verified[(i-s)]
                s=s+1
            i=i+1
        with open('../database/list.json','w') as f:
            f.write(json.dumps(self.products_verified, indent=4))

    def verif_files(self):
        if os.path.exists('../database/list.json'):
            self.verif =True
        else:
            self.verif=False






            #self.list_products.update(self.products)



            #self.products.append(self.dict)
            #self.products.append(self.products)
            #e = 0
        #    for element in self.products:
        #        self.products[e]['categories'] = item
        #        e = e + 1
        #    self.list_products.append(self.products)
