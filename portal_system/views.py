from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request=request, template_name='home.html')

def teachers(request):
    return render(request=request, template_name='teacher_course.html')