from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        role = request.POST['role']
        
        if role.strip().lower() == 'student':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            
            if not name or not email or not password:
                messages.error(request=request, message='All Fields are required.')
                return redirect('signup')
            
            if User.objects.filter(username=email).exists():
                messages.error(request=request, message='Email already exists..')
                return redirect('signup')
            
            user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
            Profile.objects.create(role=role, user=user)
            
            return render(request=request, template_name='login.html')
        
        else:
            print("Role: Teacher")
    
    return render(request=request, template_name='signup.html')



def learn_more(request):
    return render(request=request, template_name='learn_more.html')