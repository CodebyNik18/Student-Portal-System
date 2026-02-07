from django.urls import path
from . import views

urlpatterns = [
    path('add_assignments/', views.add_assignments, name='add_assignments'),
]