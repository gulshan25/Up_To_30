from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def function1(request):
    return HttpResponse('This is my first Django view')

def welcome(request,name):
    return HttpResponse(f'Hello {name}')

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


async def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)
    
