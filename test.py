#!/usr/bin/env python3

import sys
import re
import requests
from bs4 import BeautifulSoup
import csv
import psycopg2

def changeToHp(a):
    a = a.replace(" ", "")
    a = a.replace("k", "")
    a = int(a)
    if (a > 0) and (a < 1000):
        return 70
    elif (a >= 1000) and (a < 1500):
        return 100
    elif (a >= 1500) and (a < 2000):
        return 150
    elif (a >= 2000) and (a < 2500):
        return 220
    elif (a >= 2500) and (a < 3000):
        return 270
    elif (a >= 3000) and (a < 3500):
        return 330
    elif (a >= 3500) and (a < 4000):
        return 360
    elif (a >= 4000) and (a < 5000):
        return 390
    else:
        return 500
a=0

URL = "https://www.otomoto.pl/osobowe/uzywane/seg-mini"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

tableofCars = soup.find('div', attrs = {'class' : 'ooa-1un3d5b er8sc6m2'})
smallCars=[]

for row in tableofCars.findAll('article', attrs = {'class' : 'ooa-1ukhrp5 evg565y0'}):
    car = {}
    car['id'] = a
    a = a + 1
    car['yearOfManufacture'] = row.li.text
    car['price'] = row.find('span',attrs ={'class' : 'ooa-1bmnxg7 evg565y13'}).text
    mil = row.findAll('li')[1].text
    car['mileage'] = mil.strip(" km")
    hp = row.findAll('li')[2].text
    x = hp.strip(" cm3")
    car['HP to determine'] = changeToHp(x)
    car['typeOfFuel'] = row.findAll('li')[3].text
    car['name'] = row.find('a', attrs = {'target' : '_self'}).text
    img = row.find('img', attrs = {'class' : 'evg565y20 ooa-ep0of3'})
    car['img'] = img['src']
    car['gearBox'] = 'automatic' 
    smallCars.append(car)
    
        
URL = "https://www.otomoto.pl/osobowe/uzywane/seg-suv"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

tableofCars = soup.find('div', attrs = {'class' : 'ooa-1un3d5b er8sc6m2'})
SUVs=[]

for row in tableofCars.findAll('article', attrs = {'class' : 'ooa-1ukhrp5 evg565y0'}):
    car = {}
    car['id'] = a
    a = a + 1
    car['yearOfManufacture'] = row.li.text
    car['price'] = row.find('span',attrs ={'class' : 'ooa-1bmnxg7 evg565y13'}).text
    mil = row.findAll('li')[1].text                     
    car['mileage'] = mil.strip(" km")
    hp = row.findAll('li')[2].text
    x = hp.strip(" cm3")
    car['HP to determine'] = changeToHp(x)
    car['typeOfFuel'] = row.findAll('li')[3].text
    car['name'] = row.find('a', attrs = {'target' : '_self'}).text
    img = row.find('img', attrs = {'class' : 'evg565y20 ooa-ep0of3'})
    car['img'] = img['src']
    car['gearBox'] = 'automatic'
    SUVs.append(car)

URL = "https://www.otomoto.pl/osobowe/uzywane/seg-coupe"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

tableofCars = soup.find('div', attrs = {'class' : 'ooa-1un3d5b er8sc6m2'})
coupes=[]

for row in tableofCars.findAll('article', attrs = {'class' : 'ooa-1ukhrp5 evg565y0'}):
    car = {}
    car['id'] = a
    a = a + 1
    car['yearOfManufacture'] = row.li.text
    car['price'] = row.find('span',attrs ={'class' : 'ooa-1bmnxg7 evg565y13'}).text
    mil = row.findAll('li')[1].text
    car['mileage'] = mil.strip(" km")
    hp = row.findAll('li')[2].text
    x = hp.strip(" cm3")
    car['HP to determine'] = changeToHp(x)
    car['typeOfFuel'] = row.findAll('li')[3].text
    car['name'] = row.find('a', attrs = {'target' : '_self'}).text
    img = row.find('img', attrs = {'class' : 'evg565y20 ooa-ep0of3'})
    car['img'] = img['src']
    car['gearBox'] = 'automatic'
    coupes.append(car)


URL = "https://www.otomoto.pl/osobowe/uzywane/seg-cabrio"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

tableofCars = soup.find('div', attrs = {'class' : 'ooa-1un3d5b er8sc6m2'})
cabrios=[]

for row in tableofCars.findAll('article', attrs = {'class' : 'ooa-1ukhrp5 evg565y0'}):
    car = {}
    car['id'] = a
    a = a + 1
    car['yearOfManufacture'] = row.li.text
    car['price'] = row.find('span',attrs ={'class' : 'ooa-1bmnxg7 evg565y13'}).text
    mil = row.findAll('li')[1].text
    car['mileage'] = mil.strip(" km")
    hp = row.findAll('li')[2].text
    x = hp.strip(" cm3")
    car['HP to determine'] = changeToHp(x)
    car['typeOfFuel'] = row.findAll('li')[3].text
    car['name'] = row.find('a', attrs = {'target' : '_self'}).text
    img = row.find('img', attrs = {'class' : 'evg565y20 ooa-ep0of3'})
    car['img'] = img['src']
    car['gearBox'] = 'automatic'
    cabrios.append(car)
    
URL = "https://www.otomoto.pl/osobowe/uzywane/seg-sedan"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

tableofCars = soup.find('div', attrs = {'class' : 'ooa-1un3d5b er8sc6m2'})
sedans=[]

for row in tableofCars.findAll('article', attrs = {'class' : 'ooa-1ukhrp5 evg565y0'}):
    car = {}
    car['id'] = a
    a = a + 1
    car['yearOfManufacture'] = row.li.text
    car['price'] = row.find('span',attrs ={'class' : 'ooa-1bmnxg7 evg565y13'}).text
    mil = row.findAll('li')[1].text
    car['mileage'] = mil.strip(" km")
    hp = row.findAll('li')[2].text
    x = hp.strip(" cm3")
    car['HP to determine'] = changeToHp(x)
    car['typeOfFuel'] = row.findAll('li')[3].text
    car['name'] = row.find('a', attrs = {'target' : '_self'}).text
    img = row.find('img', attrs = {'class' : 'evg565y20 ooa-ep0of3'})
    car['img'] = img['src']
    car['gearBox'] = 'automatic'
    sedans.append(car)

URL = "https://www.otomoto.pl/osobowe/uzywane/seg-combi"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

tableofCars = soup.find('div', attrs = {'class' : 'ooa-1un3d5b er8sc6m2'})
combis=[]

for row in tableofCars.findAll('article', attrs = {'class' : 'ooa-1ukhrp5 evg565y0'}):
    car = {}
    car['id'] = a
    a = a + 1
    car['yearOfManufacture'] = row.li.text
    car['price'] = row.find('span',attrs ={'class' : 'ooa-1bmnxg7 evg565y13'}).text
    mil = row.findAll('li')[1].text
    car['mileage'] = mil.strip(" km")
    hp = row.findAll('li')[2].text
    x = hp.strip(" cm3")
    car['HP to determine'] = changeToHp(x)
    car['typeOfFuel'] = row.findAll('li')[3].text
    car['name'] = row.find('a', attrs = {'target' : '_self'}).text
    img = row.find('img', attrs = {'class' : 'evg565y20 ooa-ep0of3'})
    car['img'] = img['src']
    car['gearBox'] = 'automatic'
    combis.append(car)

conn = psycopg2.connect(
   database="cars",
   user='postgres', 
   password='postgres', 
   host='127.0.0.1', 
   port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()


cursor.execute("CREATE TABLE if not exists smallCars (id VARCHAR(255), name VARCHAR(255), img VARCHAR(255), yearOfManufacture VARCHAR(255), price VARCHAR(255), mileage VARCHAR(255), horsePower VARCHAR(255), typeOfFuel VARCHAR(255), gearBox VARCHAR(255))")
cursor.execute("CREATE TABLE if not exists SUVs (id VARCHAR(255), name VARCHAR(255), img VARCHAR(255), yearOfManufacture VARCHAR(255), price VARCHAR(255), mileage VARCHAR(255), horsePower VARCHAR(255), typeOfFuel VARCHAR(255), gearBox VARCHAR(255))")
cursor.execute("CREATE TABLE if not exists Coupes (id VARCHAR(255), name VARCHAR(255), img VARCHAR(255), yearOfManufacture VARCHAR(255), price VARCHAR(255), mileage VARCHAR(255), horsePower VARCHAR(255), typeOfFuel VARCHAR(255), gearBox VARCHAR(255))")
cursor.execute("CREATE TABLE if not exists Sedan (id VARCHAR(255), name VARCHAR(255), img VARCHAR(255), yearOfManufacture VARCHAR(255), price VARCHAR(255), mileage VARCHAR(255), horsePower VARCHAR(255), typeOfFuel VARCHAR(255), gearBox VARCHAR(255))")
cursor.execute("CREATE TABLE if not exists Combi (id VARCHAR(255), name VARCHAR(255), img VARCHAR(255), yearOfManufacture VARCHAR(255), price VARCHAR(255), mileage VARCHAR(255), horsePower VARCHAR(255), typeOfFuel VARCHAR(255), gearBox VARCHAR(255))")
cursor.execute("CREATE TABLE if not exists Cabrio (id VARCHAR(255), name VARCHAR(255), img VARCHAR(255), yearOfManufacture VARCHAR(255), price VARCHAR(255), mileage VARCHAR(255), horsePower VARCHAR(255), typeOfFuel VARCHAR(255), gearBox VARCHAR(255))")

for i in smallCars:
    if i['yearOfManufacture'].isnumeric():
        cursor.execute(" INSERT INTO smallCars (id, name, img, yearOfManufacture, price, mileage, horsePower, typeOfFuel, gearBox) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(i['id'] ,i['name'], i['img'], i['yearOfManufacture'],i['price'],i['mileage'],i['HP to determine'], i['typeOfFuel'], i['gearBox']))

for i in SUVs:
    if i['yearOfManufacture'].isnumeric():
        cursor.execute(" INSERT INTO SUVs (id, name, img, yearOfManufacture, price, mileage, horsePower, typeOfFuel, gearBox) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(i['id'] ,i['name'], i['img'], i['yearOfManufacture'],i['price'],i['mileage'],i['HP to determine'], i['typeOfFuel'], i['gearBox']))
for i in coupes:
    if i['yearOfManufacture'].isnumeric():
        cursor.execute(" INSERT INTO Coupes (id, name, img, yearOfManufacture, price, mileage, horsePower, typeOfFuel, gearBox) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(i['id'] ,i['name'], i['img'], i['yearOfManufacture'],i['price'],i['mileage'],i['HP to determine'], i['typeOfFuel'], i['gearBox']))
for i in sedans:
    if i['yearOfManufacture'].isnumeric():
        cursor.execute(" INSERT INTO Sedan (id, name, img, yearOfManufacture, price, mileage, horsePower, typeOfFuel, gearBox) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(i['id'] ,i['name'], i['img'], i['yearOfManufacture'],i['price'],i['mileage'],i['HP to determine'], i['typeOfFuel'], i['gearBox']))
for i in combis:
    if i['yearOfManufacture'].isnumeric():
        cursor.execute(" INSERT INTO Combi (id, name, img, yearOfManufacture, price, mileage, horsePower, typeOfFuel, gearBox) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(i['id'] ,i['name'], i['img'], i['yearOfManufacture'],i['price'],i['mileage'],i['HP to determine'], i['typeOfFuel'], i['gearBox']))
for i in cabrios:
    if i['yearOfManufacture'].isnumeric():
        cursor.execute(" INSERT INTO Cabrio (id, name, img, yearOfManufacture, price, mileage, horsePower, typeOfFuel, gearBox) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(i['id'] ,i['name'], i['img'], i['yearOfManufacture'],i['price'],i['mileage'],i['HP to determine'], i['typeOfFuel'], i['gearBox']))
conn.close
