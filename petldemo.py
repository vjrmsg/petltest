import os
import sys
import petl
import pymssql
import configparser
import requests
import datetime
import json
import decimal
import pandas as pd
import openpyxl
from petl import look, fromdb,fromjson,fromdicts,unpackdict,cut, todb, rename, tocsv
# get data from configuration file
config = configparser.ConfigParser()
try:
    config.read('ETLDemo.ini')
    print('read success')
except Exception as e:
    print('could not read configuration file:' + str(e))
    sys.exit()

# read settings from configuration file
url = config['CONFIG']['url']
destServer = config['CONFIG']['server']
destDatabase = config['CONFIG']['database']
user =  config['CONFIG']['user']
password =  config['CONFIG']['password']

# request data from URL
try:
    UserResponse = requests.get(url,verify=False)
    print ('UserResponse')
    print(destDatabase)
except Exception as e:
    print('could not make request:' + str(e))
    sys.exit()

#Extract
if (UserResponse.status_code == 200):
   data = json.loads(UserResponse.text)
   print(data)
   #data = json.loads(jsonurl.read())
   users_table = fromdicts(data)
   users_table

   users_table = unpackdict(users_table, 'address')
   users_table = unpackdict(users_table, 'geo')

    #select a few columns
   users_table = cut(users_table, 'id', 'name','username','email','phone','city','street','suite','lat','lng')

    #rename column headers
   users_table = rename(users_table, {'name':'Name','username':'Username','email':'Email','phone':'Phone','city':'City','street':'Street','suite':'Suite','lat':'Latitude', 'lng':'Longitude'})

   print(users_table)
    

   tocsv(users_table, 'users.csv')
   users_dataFrame = pd.read_csv('users.csv')
    #expenses = petl.io.xlsx.fromxlsx('Expenses.xlsx',sheet='Github')
   print(users_dataFrame.head())
# load expense document
   try:
        userrecs = petl.io.csv.fromcsv('users.csv')
        #print(userrecs.head())
   except Exception as e:
        print('could not open expenses.xlsx:' + str(e))
        sys.exit()
   try:
        dbConnection = pymssql.connect(user=user,password=password,server=destServer,database=destDatabase)
   except Exception as e:
        print('could not connect to database:' + str(e))
        sys.exit()

    # populate Expenses database table
   try:
        petl.io.todb (userrecs,dbConnection,'users')
        print ('***** User csv data successfully imported into ENT-AP-VJTEST1 SQLServer *****')
   except Exception as e:
        print('could not write to database:' + str(e))
        print (userrecs)

