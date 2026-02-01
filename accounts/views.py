from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from faker import Faker
from django.core.mail import send_mail
from django.utils import timezone   
from django.contrib.auth import authenticate, login


def signup(request):
    
    # if request.method == 'GET' and not request.session.get('otp_verified'):
    #     request.session.pop('name', None)
    #     request.session.pop('email', None)
    #     request.session.pop('institute_email', None)
        
    if request.method == 'POST':
        print("POST data: ", request.POST)
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
            
            request.session.pop('name', None)
            request.session.pop('email', None)
            request.session.pop('password', None)
            request.session.pop('institute_email', None)
            request.session.pop('teacher_otp', None)
            request.session.pop('time', None)
                        
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
                return redirect('signup')
                
            if institute_email.lower().strip() == 'ashumanager77@gmail.com':
                if action == 'send_otp':
                    faker = Faker()
                    otp_fake = faker.random_number(digits=6, fix_len=True)
                    
                    request.session['teacher_otp'] = otp_fake
                    request.session['time'] = timezone.now().timestamp()
                    request.session['institute_email'] = institute_email
                    request.session['name'] = name
                    request.session['email'] = email
                    request.session['password'] = password
                    
                    send_mail(
                        subject='OTP Request',
                        message=f'Your OTP for teacher Sign up {otp_fake}',
                        from_email='student@portal.com', 
                        recipient_list=[institute_email],
                        fail_silently=False
                    )
                    messages.success(request=request, message='OTP sent to mail successfully..')
                    return redirect('signup')
                
                elif action == 'verify_otp':
                    print(action)
                    otp_time = request.session.get('time')
                    input_otp = otp
                    generated_otp = request.session.get('teacher_otp')
                    
                    if not generated_otp or not otp_time:
                        messages.error(request=request, message='Request for OTP First...')
                        return redirect('signup')
                    
                    total_time = timezone.now().timestamp()-otp_time
                    
                    if not input_otp:
                        messages.error(request=request, message='Enter OTP for verification...')
                        return redirect('signup')
                    
                    input_otp = str(input_otp).strip()
                    
                    if total_time > 300:
                        messages.error(request=request, message='Time Expired...')
                        return redirect('signup')
                        
                    if input_otp != str(generated_otp):
                        messages.error(request=request, message='Invalid OTP...')
                        return redirect('signup')
                        
                    request.session['otp_verified'] = True
                    messages.success(request=request, message='OTP Verified...')
                    return redirect('signup')
                 
                else:
                    if request.session['otp_verified']:
                        user = User.objects.create_user(
                            username=email,
                            email=email,
                            password=password,
                            first_name=name
                        )
                        
                        Profile.objects.create(
                            user=user,
                            role=role,
                            institute_email=institute_email,
                            is_teacher_verified=True
                        )
                        
                        request.session.pop('name', None)
                        request.session.pop('email', None)
                        request.session.pop('password', None)
                        request.session.pop('institute_email', None)
                        request.session.pop('teacher_otp', None)
                        request.session.pop('time', None)
                        
                        messages.success(request=request, message='Account Created successfully, You can login now...')
                        return redirect('login')
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
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request=request, username=email, password=password)
        
        if user:
            
            profile = user.profile
            role = profile.role
            teacher_verified = profile.is_teacher_verified
            
            if role.lower().strip() == 'student':
                return HttpResponse('Student Dashboard')
            
            elif role.lower().strip() == 'teacher' and teacher_verified:
                return HttpResponse('Teacher Dashboard')
            
            else:
                messages.error(request=request, message='Teacher is not verified...')
                return redirect('login')
            
        else:
            messages.error(request=request, message='Invalid Details..')
            return redirect('login')
        
    return render(request=request, template_name='login.html')

def learn_more(request):
    return render(request=request, template_name='learn_more.html')