from urllib import request
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    #name은 DTL로 url링크 부를때 사용
    #{% url 'app_name:name}
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
