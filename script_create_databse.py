#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system
import mysql.connector


bdd = mysql.connector.connect(host="192.168.1.77",user="student",password="wired")
cursor = bdd.cursor()


for line in open('packages/database/create_database.sql').read().split(';\n'):
    cursor.execute(line)
