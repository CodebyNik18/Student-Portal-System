from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    COURSE_CHOICES = [
        ('AIML', 'Artificial Intelligence and Machine Learning'),
        ('CORE', 'Computer Science Core'),
        ('IT', 'Information Technology'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(blank=False, choices=COURSE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)