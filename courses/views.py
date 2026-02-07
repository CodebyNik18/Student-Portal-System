from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from assignments.models import Assignment

def dashboard(request):
    name = request.user
    course = Course.objects.get(user=name).get_course_display()
    assignments = Assignment.objects.filter(course_name=Course.objects.get(user=name).course)
    context = {
        'name': name.get_full_name().capitalize(),
        'course': course,
        'assignments': assignments,
    }
    return render(request=request, template_name='teacher_home.html', context=context)
