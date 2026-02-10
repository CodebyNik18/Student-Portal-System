from django.urls import path, include
from . import views

urlpatterns = [
    path('teacher_dashboard/', views.dashboard, name='dashboard'),
    path('teacher_dashboard/', include('assignments.urls')),
]