from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Assignment

def add_assignments(request):
    if request.method == 'POST':
        title = request.POST['title']
        due_date = request.POST['due_date']
        pdf = request.FILES['pdf']
        course = request.user.course_set.get(user=request.user).course
        name = request.user
        Assignment.objects.create(
            teacher_name=name,
            course_name=course,
            title=title,
            assignment=pdf,
            due_date=due_date
        )
        return redirect('dashboard')
    return render(request=request, template_name='add_assignment.html')