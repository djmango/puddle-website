from django.shortcuts import render
from django.http import HttpResponse

# views

def index(request):
    return HttpResponse("What a placeholder")
