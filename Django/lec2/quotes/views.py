from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Quote

# Create your views here.
quotes = [
    'Quote 1',
    'Quote 2',
]

def quotes_list(request:HttpRequest):
    quotes = Quote.objects.all().order_by('-year')
    return render(request, 'quotes/list.html', {'quotes': quotes})


def edit_quote(request:HttpRequest, id:int):
    quote = Quote.objects.get(id=id)
    errors = {}
    if request.method == 'GET':
        return render(request, 'quotes/edit.html', {'quote': quote})
    else:
        author = request.POST.get('author')
        if not author:
            errors['author'] = 'No Author'
            return render(request, 'quotes/edit.html', {'quote': quote, 'errors': errors})
        quote.author = author
        quote.quote = request.POST.get('quote', quote.quote)
        quote.year = request.POST.get('year', quote.year)

        quote.save()
        

def delete_quote(request:HttpRequest, id:int):
    quote = Quote.objects.get(id=id)
    quote.delete()
    return HttpResponseRedirect('/quotes')


@csrf_exempt
def add(request:HttpRequest):
    if request.method == 'POST':
        quote = request.POST.get('quote')
        if quote:
            quotes.append(quote)
            return HttpResponse('Quote added')
        else:
            return HttpResponseBadRequest('Quote is empty')
    else:
         return HttpResponseBadRequest('POST Only')  