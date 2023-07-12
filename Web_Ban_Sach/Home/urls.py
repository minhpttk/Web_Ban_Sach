from django.urls import path
from . import views
app='Home'
urlpatterns = [
    path('',views.index,name="index")

]
