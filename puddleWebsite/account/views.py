import json

import MySQLdb
from django.http import HttpResponse
from django.shortcuts import render

# pull keys
SQL_HOST = json.loads(open('keys.json').read())['sqlTestHost']
SQL_PASSWD = json.loads(open('keys.json').read())['sqlTest1Pass']

# mysql setup
mysql = MySQLdb.connect(host=SQL_HOST, user='test1',
                        passwd=SQL_PASSWD, port=3306, db='test1', charset='utf8')
mysqlcon = mysql.cursor()

# views


def index(request):
    """shows profile index upon request

    Arguments:
        request {string} -- managed by django
    """

    return render(request, 'profile_index.html', content_type='text/html')

