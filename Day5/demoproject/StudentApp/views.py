from django.shortcuts import render
from StudentApp.models import Student


# Create your views here.
def home(request):
    context={'title':'Home'}
    return render(request, 'home.html',context)

def home(request):
    context={'students':students}
    return render(request, 'index.html',context)