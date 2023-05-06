from django.shortcuts import render
from .models import Project, Classes, Sword_img
# Create your views here.
def home(request):
    projects = Project.objects
    swords = Sword_img.objects
    return render(request, 'projects/home.html', {'projects': projects, 'swords': swords})

def about(request):
    return render(request, 'projects/about.html')

def classes(request):
    classes = Classes.objects
    return render(request, 'projects/classes.html', {'classes': classes})