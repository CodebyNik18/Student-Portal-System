from django.urls import path
from . import views

urlpatterns = [
    path('add_assignments/', views.add_assignments, name='add_assignments'),
    path('edit_assignments/<int:pk>', views.edit_assignments, name='edit_assignments'),
    path('delete_assignments/<int:pk>', views.delete_assignments, name='delete_assignments')
]