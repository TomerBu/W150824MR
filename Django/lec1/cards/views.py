from django.shortcuts import render
from django.http import HttpResponse

# views are functions that take a web request and return a web response

def index(request):
    return HttpResponse("Hello, world. You're at the cards index.")
