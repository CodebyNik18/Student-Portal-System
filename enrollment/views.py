from django.shortcuts import render
from .models import Enrollment


def dashboard(request):
    user = request.user
    course = Enrollment.objects.get(user=user).get_course_display()
    context = {
        'user': user.get_full_name().capitalize(),
        'course': course
    }
    return render(request=request, template_name='student_dashboard.html', context=context)