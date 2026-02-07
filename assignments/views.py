from django.shortcuts import render
from django.http import HttpResponse

def add_assignments(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
    return render(request=request, template_name='add_assignment.html')