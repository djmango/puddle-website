import json
import random

import sqlite3
from django.http import HttpResponse
from google.auth.transport import requests
from google.oauth2 import id_token

# pull keys
CLIENT_ID = json.loads(open('keys.json').read())['googleoauthid']

# db setup
db = sqlite3.connect('db.sqlite')
dbcon = db.cursor()


def verify(request):
    """google oauth login verification and account creation

    Arguments:
        request {json} -- managed by django
    """
    try:
        token = request.POST.get('idtoken')
        userInfo = id_token.verify_oauth2_token(
            token, requests.Request(), CLIENT_ID)

        if userInfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        # store user info in session
        request.session['userInfo'] = userInfo

        # check if the user already exists in db
        dbcon.execute("""SELECT * FROM account_users WHERE EXISTS (SELECT email FROM account_users WHERE email = '%s');""" % userInfo['email'])
        r = dbcon.fetchone()
        if r is None:  # if this is a new account, add userInfo to the db
            # generate a unique id
            random.seed(dbcon.execute("""SELECT * from account_users""")) # seed based on number of users, so no repeats
            userId = random.randint(9999999999999999999999999999999, 100000000000000000000000000000000) # generate a 32 int long uid
            
            # upload userInfo to db
            holder = "meh" # temp
            dbcon.execute(
                """INSERT INTO account_users (userId, email, name, picture, settings)
                VALUES (%s, %s, %s, %s, %s);""",
                (userId, userInfo['email'], userInfo['name'], userInfo['picture'], holder))
            db.commit()
        jsonResponse = json.dumps({"picture": userInfo['picture'], "name": userInfo['name']})
        return HttpResponse(jsonResponse)

    except ValueError:
        # Invalid token
        pass
