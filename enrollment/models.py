from django.db import models
from django.contrib.auth.models import User



class Enrollment(models.Model):
    COURSE_CHOICES = [
        ('AIML', 'Artificial Intelligence and Machine Learning'),
        ('CORE', 'Computer Science Core'),
        ('IT', 'Information Technology'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(choices=COURSE_CHOICES, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.user.get_full_name()