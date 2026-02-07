from django.contrib import admin
from .models import Assignment



class AssignmentDisplay(admin.ModelAdmin):
    list_display = [
        'name', 'course_name'
    ]
    
    def name(self, obj):
        return obj.teacher_name.get_full_name()
admin.site.register(Assignment, AssignmentDisplay)