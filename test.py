#!/usr/bin/env python3

import sys
import re
import requests
from bs4 import BeautifulSoup
import csv
import psycopg2


URL = "https://www.otomoto.pl/osobowe/uzywane/seg-mini?search%5Badvanced_search_expanded%5D=true"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

tableofCars = soup.find('div', attrs = {'class' : 'ooa-1un3d5b er8sc6m2'})
smallCars=[]

for row in tableofCars.findAll('article', attrs = {'class' : 'ooa-1nix3k0 evg565y0'}):
    car = {}
    car['yearOfManufacture'] = row.li.text
    car['price'] = row.find('span',attrs ={'class' : 'ooa-1bmnxg7 evg565y11'}).text
    mil = row.findAll('li')[1].text
    car['mileage'] = mil.strip(" km")
    hp = row.findAll('li')[2].text
    car['HP to determine'] = hp.strip(" cm3")
    car['typeOfFuel'] = row.findAll('li')[3].text
    smallCars.append(car)
        
URL = "https://www.otomoto.pl/osobowe/uzywane/seg-suv?search%5Badvanced_search_expanded%5D=true"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

tableofCars = soup.find('div', attrs = {'class' : 'ooa-1un3d5b er8sc6m2'})
SUVs=[]

for row in tableofCars.findAll('article', attrs = {'class' : 'ooa-1nix3k0 evg565y0'}):
    car = {}
    car['yearOfManufacture'] = row.li.text
    car['price'] = row.find('span',attrs ={'class' : 'ooa-1bmnxg7 evg565y11'}).text
    mil = row.findAll('li')[1].text
    car['mileage'] = mil.strip(" km")
    hp = row.findAll('li')[2].text
    car['HP to determine'] = hp.strip(" cm3")
    car['typeOfFuel'] = row.findAll('li')[3].text
    SUVs.append(car)


URL = "https://www.otomoto.pl/osobowe/uzywane/seg-coupe?search%5Badvanced_search_expanded%5D=true"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

tableofCars = soup.find('div', attrs = {'class' : 'ooa-1un3d5b er8sc6m2'})
coupes=[]

for row in tableofCars.findAll('article', attrs = {'class' : 'ooa-1nix3k0 evg565y0'}):
    car = {}
    car['yearOfManufacture'] = row.li.text
    car['price'] = row.find('span',attrs ={'class' : 'ooa-1bmnxg7 evg565y11'}).text
    mil = row.findAll('li')[1].text
    car['mileage'] = mil.strip(" km")
    hp = row.findAll('li')[2].text
    car['HP to determine'] = hp.strip(" cm3")
    car['typeOfFuel'] = row.findAll('li')[3].text
    coupes.append(car)
 
conn = psycopg2.connect(
   database="cars",
   user='postgres', 
   password='postgres', 
   host='127.0.0.1', 
   port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

#Preparing query to create a database 
#TO BE COMMENTED IF YOU WANT TO RUN THE SCRIPT MULTIPLE TIMES
#cursor.execute ("CREATE database car")

cursor.execute("CREATE TABLE if not exists smallCars (yearOfManufacture VARCHAR(255), price VARCHAR(255), mileage VARCHAR(255), HP VARCHAR(255), typeOfFuel VARCHAR(255))")
cursor.execute("CREATE TABLE if not exists SUVs (yearOfManufacture VARCHAR(255), price VARCHAR(255), mileage VARCHAR(255), HP VARCHAR(255), typeOfFuel VARCHAR(255))")
cursor.execute("CREATE TABLE if not exists Coupes (yearOfManufacture VARCHAR(255), price VARCHAR(255), mileage VARCHAR(255), HP VARCHAR(255), typeOfFuel VARCHAR(255))")

for i in smallCars:
    if i['yearOfManufacture'].isnumeric():
        cursor.execute(" INSERT INTO smallCars (yearOfManufacture, price, mileage, HP, typeOfFuel) VALUES(%s, %s, %s, %s, %s)",(i['yearOfManufacture'],i['price'],i['mileage'],i['HP to determine'], i['typeOfFuel']))

for i in SUVs:
    if i['yearOfManufacture'].isnumeric():
        cursor.execute(" INSERT INTO SUVs (yearOfManufacture, price, mileage, HP, typeOfFuel) VALUES(%s, %s, %s, %s, %s)",(i['yearOfManufacture'],i['price'],i['mileage'],i['HP to determine'], i['typeOfFuel']))

for i in coupes:
    if i['yearOfManufacture'].isnumeric():
        cursor.execute(" INSERT INTO Coupes (yearOfManufacture, price, mileage, HP, typeOfFuel) VALUES(%s, %s, %s, %s, %s)",(i['yearOfManufacture'],i['price'],i['mileage'],i['HP to determine'], i['typeOfFuel']))

conn.close
