from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

names = ['Alice', 'Bob', 'Charlie']

@csrf_exempt # ביטול ההגנה באופן זמני
def add_name(request:HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            names.append(name)
        else:
            return HttpResponseBadRequest('Name is required!')
        
        return HttpResponse('Name added successfully!')
    else:
        return HttpResponseBadRequest("POST Only with name please")
       
def get_names(request:HttpRequest):
    return HttpResponse(", ".join(names))

from django.shortcuts import render

def get_html(request:HttpRequest):
    return render(request, 'students/list.html',  {'names': names})

def add_html(request:HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')

        if name:
            names.append(name)
            return HttpResponseRedirect('/students/get')
        else:
            return HttpResponseBadRequest('Name is required!')
        
    return render(request, 'students/add.html')

def edit_html(request:HttpRequest, id:int):
    if id in range(len(names)) and request.method == 'GET':
        name = names[id]
        return render(request, 'students/edit.html', {'name': name, 'id': id})
    
    if id in range(len(names)) and request.method == 'POST':
        name = request.POST.get('name')
        names[id] = name
        return HttpResponseRedirect('/students/get')
    
    else:
        return HttpResponseBadRequest('Invalid ID')
    

from students.models import Student

def view_list_db(request:HttpRequest):
    students = Student.objects.all()
    return render(request, 'students/list_db.html', {'students': students})