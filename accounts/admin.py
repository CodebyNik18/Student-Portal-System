from django.contrib import admin
from .models import Profile
from .models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 'role'
    ]
admin.site.register(Profile, ProfileAdmin)