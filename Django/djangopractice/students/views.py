from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

names = ['Alice', 'Bob', 'Charlie']

@csrf_exempt # ביטול ההגנה באופן זמני
def add_name(request:HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        names.append(name)
    return HttpResponse('Name added successfully!')
       
def get_names(request:HttpRequest):
    return HttpResponse(",".join(names))

def foo(request):
    return HttpResponse('Foo!!!')

def bar(request):
    return HttpResponse('Bar!!!')