from django.shortcuts import render
from StudentApp.models import Student

# Create your views here.

def index(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'index.html',context)
