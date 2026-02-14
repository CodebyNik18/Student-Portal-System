from django.shortcuts import render
from .models import Enrollment
from assignments.models import SubmitAssignment, Assignment


def dashboard(request):
    user = request.user
    course = Enrollment.objects.get(user=user)
    assignments = Assignment.objects.filter(course_name=course.course)
    submitted_assignments_id = SubmitAssignment.objects.filter(user=user).values_list('assignment_id', flat=True)
    pending_assignments = assignments.exclude(id__in=submitted_assignments_id)
    submitted_assignments = SubmitAssignment.objects.filter(user=user)
    context = {
        'user': user.get_full_name().capitalize(),
        'course': course.get_course_display(),
        'pending_assignments': pending_assignments,
        'submitted_assignments': submitted_assignments,
    }
    return render(request=request, template_name='student_dashboard.html', context=context)