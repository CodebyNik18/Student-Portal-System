from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('learn_more/', views.learn_more, name='learn_more'),
    path('login/', views.login_, name='login_'),
    path('courses/', views.courses, name='courses')
]