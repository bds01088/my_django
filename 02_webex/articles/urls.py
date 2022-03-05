from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), 
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
]
