import json
import MySQLdb
from argon2 import PasswordHasher
from django.http import HttpResponse
from django.shortcuts import render

# pull keys
keys = json.loads(open('keys.json').read())

# mysql setup
mysql = MySQLdb.connect(host=keys['sqlTestHost'], user='test1', passwd=keys['sqlTest1Pass'], port=3306, db='test1', charset='utf8')
mysqlcon = mysql.cursor()

# functions

def hash(passwd):
    hashed = PasswordHasher().hash(passwd)
    # PasswordHasher().verify(hashed, passwd)
    return hashed

# views

def index(request):
    return HttpResponse(hash("efdddddddddd%"))
