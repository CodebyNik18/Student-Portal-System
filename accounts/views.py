from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from faker import Faker
from django.core.mail import send_mail
from django.utils import timezone   

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
            
            messages.success(request=request, message='Account created Successfully...You can now login')
            return redirect('login')
        
        else:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            institute_email = request.POST['institute_email']
            otp = request.POST['otp']
            action = request.POST['action']
            
            if not name or not email or not password or not institute_email:
                messages.error(request=request, message='All fields are required..')
                return redirect('signup')
            
            if User.objects.filter(username=email).exists():
                messages.error(request=request, message='Email already exists...')
                
            if institute_email.lower().strip() == 'ashumanager77@gmail.com':
                if action == 'send_otp':
                    faker = Faker()
                    otp_fake = faker.random_number(digits=6, fix_len=True)
                    
                    request.session['teacher_otp'] = otp_fake
                    request.session['time'] = timezone.now().timestamp()
                    request.session['institute_email'] = institute_email
                    request.session['name'] = name
                    request.session['email'] = email
                    
                    send_mail(
                        subject='OTP Request',
                        message=f'Your OTP for teacher Sign up {otp_fake}',
                        from_email='student@portal.com', 
                        recipient_list=[institute_email],
                        fail_silently=False
                    )
                    messages.success(request=request, message='OTP sent to mail successfully..')
                    return redirect('signup')
                
            else:
                messages.error(request=request, message='Enter valid Institue Email..')
                return redirect('signup')
            
    context = {
        'name': request.session.get('name', ''),
        'email': request.session.get('email', ''),
        'institute_email': request.session.get('institute_email', ''),
    }
    return render(request=request, template_name='signup.html', context=context)

def login(request):
    return render(request=request, template_name='login.html')

def learn_more(request):
    return render(request=request, template_name='learn_more.html')