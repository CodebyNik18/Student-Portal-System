from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request=request, template_name='signup.html')

def learn_more(request):
    return render(request=request, template_name='learn_more.html')