from django.shortcuts import render


# Create your views here.

def home(request):
    data = {
        'title': 'Home',
        'author' : 'Gulshan Rahman',
        'heading' : 'Welcome to Gulshan\'s Blog',
    }

    students = [
        {'id' : 1, 'name' : 'Afrin Sultana', 'email' : 'afrin@gmail.com', 'phone': '01723456789'},
        {'id' : 2, 'name' : 'Nashid Pervez', 'email' : 'nashid@gmail.com', 'phone': '01723456789'},
        {'id' : 3, 'name' : 'Shiddhartho Karmokar', 'email' : 'sid@gmail.com', 'phone': '01723456789'},
        {'id' : 4, 'name' : 'Shahin Rahim', 'email' : 'shahin@gmail.com', 'phone': '01723456789'},
        {'id' : 5, 'name' : 'Nowshin Anjum Kader', 'email' : 'nowshin@gmail.com', 'phone': '01723456789'},
        {'id' : 6, 'name' : 'Gulshan Rahman', 'email' : 'g.r.tanny@gmail.com', 'phone': '01746511536'},
        {'id' : 7, 'name' : 'Tahmed Hossain', 'email' : 'tahmed@gmail.com', 'phone': '01723456789'},
        {'id' : 8, 'name' : 'Mehedi Hasan', 'email' : 'mehedi@gmail.com', 'phone': '01723456789'},
    ]

    

    context = {
        'data' : data, 'students' : students

    }
    return render(request, 'home.html', context)

def contact(request):
    context= {} 
    return render(request,'contact.html',context)
    
def about(request):
    context= {} 
    return render(request,'about.html',context)
