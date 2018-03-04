from django.shortcuts import render
from django.http import HttpResponse
from argon2 import PasswordHasher

# functions

def hash(passwd):
    hash = PasswordHasher().hash(passwd)
    PasswordHasher().verify(hash, passwd)

# views

def index(request):
    return HttpResponse("What a placeholder")

