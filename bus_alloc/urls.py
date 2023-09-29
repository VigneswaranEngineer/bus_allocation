from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.login,name=''),
    path('registration.html',views.registration,name=''),
]