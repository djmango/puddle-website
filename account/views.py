import json

import sqlite3
from django.http import HttpResponse
from django.shortcuts import render

# db setup
db = sqlite3.connect('db.sqlite')
dbcon = db.cursor()

# views
def index(request):
    """shows profile index upon request

    Arguments:
        request {string} -- managed by django
    """

    return render(request, 'profile_index.html', content_type='text/html')

