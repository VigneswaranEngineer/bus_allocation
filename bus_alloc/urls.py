from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.login,name=''),
    path('registration',views.registration,name=''),
    path('userpage',views.userpage,name=''),
]