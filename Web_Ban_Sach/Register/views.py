from django.shortcuts import render
from django.http import HttpResponse
from .form import registerForm
# Create your views here.

def index(request):
    rf = registerForm
    return render(request,'Register/index.html',{'rf':rf})
def 