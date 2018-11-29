import requests
import mysql.connector
import json

r=requests.get('https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=biscuits&page_size=500&sort_by=unique_scans_n&countries=France&json=1')
dict = r.json()
#print(dict)
products= dict['products']



bdd = mysql.connector.connect(host="192.168.1.77",user="student",password="wired", database="pur_beurre")
cursor = bdd.cursor()
i=0





for item in products:

    if ('nutrition_grade_fr' or
        'brands' or
         'product_name' or
          'url') not in products[i]:
        del products[i]
    else:
        cursor.execute("INSERT INTO Product (name_product, brand_product, nutritional_note, link_open_food_fact) VALUES (%s, %s, %s, %s)",
        (products[i]['product_name'], products[i]['brands'],
        products[i]['nutrition_grade_fr'], products[i]['url']))
        i=i+1
        print(i)

bdd.commit()
