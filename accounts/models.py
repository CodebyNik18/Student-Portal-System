from django.db import models
from django.contrib.auth.models import User
from faker import Faker

# Create your models here.
def random_otp():
    faker = Faker()
    return faker.random_number(digits=6, fix_len=True)


class Profile(models.Model):
    
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(default='student', max_length=15, choices=ROLE_CHOICES)
    institute_email = models.EmailField(blank=True, null=True)

    otp = models.IntegerField(blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    is_teacher_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)