from django.contrib import admin
from .models import Enrollment


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 'course'
    ]
    
    
    def full_name(self, obj):
        return obj.user.get_full_name()
admin.site.register(Enrollment, EnrollmentAdmin)