from django.core.mail import send_mail

from django.shortcuts import render, get_object_or_404, redirect

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
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            city = form.cleaned_data['city']
            state_or_province = form.cleaned_data['state_or_province']
            zip_code = form.cleaned_data['zip_code']
            country = form.cleaned_data['country']
            phone_number = form.cleaned_data['phone_number']
            depth_of_sori = form.cleaned_data['depth_of_sori']
            length_of_blade = form.cleaned_data['length_of_blade']
            type_of_steel = form.cleaned_data['type_of_steel']
            other_specifications = form.cleaned_data['other_specifications']

            send_mail('order form for blade', 'this is the order', ['rechkemmer3@gmail.com'] )

            return redirect('order_form')
    else:
        form = OrderForm()
    return render(request, 'projects/order_form.html', {'form': form})


def details_h(request, hotel_id):
    hotel_details = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'projects/details_h.html', {'hotel': hotel_details})


def sales(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)

        if form.is_valid():
            print('the form was valid')

            return redirect('sales')
    else:
        form = SalesForm()
    sword_sales = Sword_sales.objects
    return render(request, 'projects/sales.html', {'sword_sales': sword_sales, "form": form})


def details_sales(request, sword_sales_id):
    sword_sales_detail = get_object_or_404(Sword_sales, pk=sword_sales_id)
    return render(request, 'projects/details_sales.html', {'sword_sales_detailes': sword_sales_detail})
