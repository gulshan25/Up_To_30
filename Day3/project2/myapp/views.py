from django.shortcuts import render

# Create your views here.

def home(request):
    data = {
        'title': 'Home',
        'author': 'Gulshan Rahman',
        'heading': 'Welcome to Gulshan\'s Blog',
    }

    students = [
        {'id': 1,'name': 'Afrin Sultana', 'email': 'afrin@gmail.com', 'phone': '01746511536'},
        {'id': 2,'name': 'Nashid Pervez', 'email': 'nashid@gmail.com', 'phone': '01746511536'},
        {'id': 3,'name': 'Mehedi Hasan', 'email': 'mehedi@gmail.com', 'phone': '01746511536'},
        {'id': 4,'name': 'Tahmed Hossain', 'email': 'tahmed@gmail.com', 'phone': '01746511536'},
        {'id': 5,'name': 'Siddarth Kormokar', 'email': 'sid@gmail.com', 'phone': '01746511536'},
        {'id': 6,'name': 'Nowrin Kader', 'email': 'nowrin@gmail.com', 'phone': '01746511536'},
        {'id': 7,'name': 'Aziz Parvez', 'email': 'aziz@gmail.com', 'phone': '01746511536'},
        {'id': 8,'name': 'Gulshan Rahman', 'email': 'g.r.tanny@gmail.com', 'phone': '01746511536'},
    ]


    context = {
        'data' : data, 'students' : students 

    }
    return render(request, 'home.html', context)
    
