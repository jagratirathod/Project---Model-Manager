from django.shortcuts import render
from django.http import HttpResponse
from.models import *

# Create your views here.

def hello(request):
    return HttpResponse("Hello world !")


def home(request):  
    # result=Student.objects.all()
    # result=Student.student.all()
    result=Student.custom.get_stu_roll_range(101,104)
    return render(request,"home1.html",{'result':result})