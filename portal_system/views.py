from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import Course
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request=request, template_name='home.html')

def teachers(request):
    
    if request.method == 'POST':
        
        user = request.user
        subject = request.POST['course']
        role = '' if user.is_superuser else user.profile.role    #   Short Hand if-else statements
        
        if (role.lower().strip() == 'teacher') and (request.user.profile.is_teacher_verified):
            
            if Course.objects.filter(user=user).exists():
                Course.objects.filter(user=user).update(course=subject)
                return redirect('dashboard')
            
            else:
                Course.objects.create(user=user, course=subject)
                return redirect('dashboard')
            
        else:
            messages.error(request=request, message='Only verified teachers are allowed to select courses.')
            return redirect('login_')
            
    return render(request=request, template_name='teacher_course.html')