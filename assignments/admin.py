from django.contrib import admin
from .models import Assignment, SubmitAssignment



class AssignmentAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'course_name'
    ]
    
    def name(self, obj):
        return obj.teacher_name.get_full_name()
admin.site.register(Assignment, AssignmentAdmin)


class SubmitAssignmentAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
    
    def name(self, obj):
        return obj.user.get_full_name()
admin.site.register(SubmitAssignment, SubmitAssignmentAdmin)