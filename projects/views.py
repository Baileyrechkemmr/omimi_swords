from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'projects/home.html')

def about(request):
    return render(request, 'projects/about.html')

def classes(request):
    return render(request, 'projects/classes.html')