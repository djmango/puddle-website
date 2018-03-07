import json

from django.http import HttpResponse
from google.auth.transport import requests
from google.oauth2 import id_token

# pull keys
CLIENT_ID = json.loads(open('keys.json').read())['googleoauthid']

# (Receive token by HTTPS POST)
# ...

def verify(request):
    """google oauth login verification
    
    Arguments:
        request {json} -- managed by django
    """
    try:
        token = request.POST.get('idtoken')
        userInfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        if userInfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        return HttpResponse(userInfo['email'])

    except ValueError:
        # Invalid token
        pass
