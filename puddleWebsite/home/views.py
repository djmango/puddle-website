from django.http import HttpResponse
from django.shortcuts import render

# views

def index(request):
    """shows homepage upon request
    
    Arguments:
        request {string} -- managed by django
    """
    
    return render(request, 'home.html', content_type='text/html')
