from django.urls import path
from StudentApp import views

urlpatterns = [
    path('index/', views.index,name='index'),
]