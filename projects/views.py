from django.shortcuts import render, get_object_or_404

from .forms import ClassesForm, OrderForm, SalesForm

from .models import Year, Classes, Sword_img, Hotel, Blog, Sword_sales
# Create your views here.


def home(request):
    swords = Sword_img.objects
    return render(request, 'projects/home.html', {'swords': swords})


def about(request):
    return render(request, 'projects/about.html')


def classes(request):
    if request.method == 'POST':
        form = ClassesForm(request.POST)

        if form.is_valid():
            print('the form was valid')

            return render(request, 'projects/classes.html')
    else:
        form = ClassesForm()
    
    year = Year.objects
    classes = Classes.objects
    hotel = Hotel.objects
    return render(request, 'projects/classes.html', {'classes': classes, 'hotel': hotel, 'year': year, "form": form})


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
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            print('the form was valid')

            return render(request, 'projects/order_form.html')
    else:
        form = OrderForm()
    return render(request, 'projects/order_form.html')


def details_h(request, hotel_id):
    hotel_details = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'projects/details_h.html', {'hotel': hotel_details})


def sales(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)

        if form.is_valid():
            print('the form was valid')

            return render(request, 'projects/sales.html')
    else:
        form = SalesForm()
    sword_sales = Sword_sales.objects
    return render(request, 'projects/sales.html', {'sword_sales': sword_sales})


def details_sales(request, sword_sales_id):
    sword_sales_detail = get_object_or_404(Sword_sales, pk=sword_sales_id)
    return render(request, 'projects/details_sales.html', {'sword_sales_detailes': sword_sales_detail})
