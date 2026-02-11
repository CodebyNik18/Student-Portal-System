from django.shortcuts import render
from .models import Enrollment
from assignments.models import SubmitAssignment, Assignment


def dashboard(request):
    user = request.user
    course = Enrollment.objects.get(user=user)
    assignments = Assignment.objects.filter(course_name=course.course)
    context = {
        'user': user.get_full_name().capitalize(),
        'course': course.get_course_display(),
        'assignments': assignments
    }
    return render(request=request, template_name='student_dashboard.html', context=context)