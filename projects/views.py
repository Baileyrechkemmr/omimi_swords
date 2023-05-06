from django.shortcuts import render
from .models import Project, Classes
# Create your views here.
def home(request):
    projects = Project.objects
    return render(request, 'projects/home.html', {'projects': projects})

def about(request):
    return render(request, 'projects/about.html')

def classes(request):
    classes = Classes.objects
    return render(request, 'projects/classes.html', {'classes': classes})