from django.shortcuts import render
from .models import Enrollment
from assignments.models import SubmitAssignment, Assignment


def dashboard(request):
    user = request.user
    course = Enrollment.objects.get(user=user).get_course_display()
    assignments = Assignment.objects.all()
    context = {
        'user': user.get_full_name().capitalize(),
        'course': course,
        'assignments': assignments
    }
    return render(request=request, template_name='student_dashboard.html', context=context)