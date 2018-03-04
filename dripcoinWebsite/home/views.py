from django.shortcuts import render
from django.http import HttpResponse

# views

def index(request):
    return render(request, 'home.html', content_type='text/html')
