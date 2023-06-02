from django.shortcuts import render, get_object_or_404
from .models import Year, Classes, Sword_img, Hotel, Blog
# Create your views here.
def home(request):
    swords = Sword_img.objects
    return render(request, 'projects/home.html', {'swords': swords})

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


def details_s(request, sword_img_id):
    sword_detail = get_object_or_404(Sword_img, pk=sword_img_id)
    return render(request, 'projects/details_s.html', {'sword': sword_detail})


def order_form(request):
    return render(request, 'projects/order_form.html')


def details_h(request, hotel_id):
    hotel_details = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'projects/details_h.html', {'hotel': hotel_details})
