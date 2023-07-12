from django.urls import path
from . import views
name = 'Register'
urlpatterns = [
    path('', views.index, name='index'),
    
]
