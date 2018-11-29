#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

class Api:
    """class used to build api requests"""
    def __init__(self):
        #self.category_request = category_request
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


    def request_api(self):
        """ create the request according to the category requested"""
        for item in self.category:
            self.querystring['tag_0'] = item
            response = requests.request("GET", self.url, headers=self.headers,
                                        params=self.querystring)
            self.dict = response.json()
            self.products = self.dict['products']
            self.list_products.append(self.products)
