from django.urls import path
from . import views
import datetime

urlpatterns = [
    path('func1/', views.function1),
    path('wc/<str:name>/', views.welcome),
    path('dt/', views.current_datetime),

]


# urlpatterns = [

#         path('history/', views.history),
#         path('edit/', views.edit),
#         path('discuss/', views.discuss),
#         path('permissions/', views.permissions),

# ]