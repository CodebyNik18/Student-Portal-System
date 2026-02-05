from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'user_first_name', 'course'
    ]
    
    def user_first_name(self, obj):
        return obj.user.first_name
    
    
admin.site.register(Course, CourseAdmin)