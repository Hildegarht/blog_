from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('post/<str:pk>',views.post,name='post'),
    path('home/<str:hm>',views.post,name='home')
]