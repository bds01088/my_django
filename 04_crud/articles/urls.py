from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    #path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    #variable routing
    path('<int:article_pk>/', views.detail, name='detail'),
    #삭제
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    #업데이트
    path('<int:article_pk>/update/', views.update, name='update'),
]