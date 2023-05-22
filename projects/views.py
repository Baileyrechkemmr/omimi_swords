from django.shortcuts import render
from .models import Year, Classes, Sword_img, Hotel, Blog
# Create your views here.
def home(request):
    year = Year.objects
    swords = Sword_img.objects
    return render(request, 'projects/home.html', {'year': year, 'swords': swords})

def about(request):
    return render(request, 'projects/about.html')

def classes(request):
    year = Year.objects
    classes = Classes.objects
    hotel= Hotel.objects
    return render(request, 'projects/classes.html', {'classes': classes, 'hotel': hotel, 'year': year})


def movie(request):
    return render(request, 'projects/movie.html')


def blog(request):
    blog = Blog.objects
    return render(request, 'projects/blog.html', {'blog': blog})


def gallery(request):
    swords = Sword_img.objects
    return render(request, 'projects/gallery.html', {'swords': swords})


def details_s(request):
    swords = Sword_img.objects
    return render(request, 'projects/details_s.html', {'swords': swords})
