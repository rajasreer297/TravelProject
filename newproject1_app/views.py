from django.http import HttpResponse
from django.shortcuts import render
from . models import  Place
from . models import Teammember
from . import views

def newproject1(request):
    obj=Place.objects.all()
    obj1=Teammember.objects.all()
    return render(request,"index.html",{'result1':obj1,'result2':obj})

