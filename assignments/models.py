from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Assignment(models.Model):
    COURSE_CHOICES = [
        ('AIML', 'Artificial Intelligence and Machine Learning'),
        ('CORE', 'Computer Science Core'),
        ('IT', 'Information Technology'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering')
    ]
    
    teacher_name = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(choices=COURSE_CHOICES)
    title = models.CharField(max_length=250)
    assignment = models.FileField(upload_to='assignment_pdfs/')
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.teacher_name.get_full_name()