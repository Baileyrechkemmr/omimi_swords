

from django.shortcuts import render, get_object_or_404, redirect

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

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
            class_name = form.cleaned_data['class_name']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            city = form.cleaned_data['city']
            state_or_province = form.cleaned_data['state_or_province']
            zip_code = form.cleaned_data['zip_code']
            country = form.cleaned_data['country']
            phone_number = form.cleaned_data['phone_number']

            html = render_to_string('projects/emails/classes.html', {
                'class_name': class_name,
                'email': email,
                'name': name,
                'address_1': address_1,
                'address_2': address_2,
                'city': city,
                'state_or_province': state_or_province,
                'zip_code': zip_code,
                'country': country,
                'phone_number': phone_number,

            })

            send_mail('form for class singe up', 'student info',
                    ['brechkemmer01@gmail.com'], html_message=html)

            return redirect('classes')
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
        email = request.POST.get('email', '')
        name = request.POST.get('name', '')
        address_1 = request.POST.get('address_1', '')
        address_2 = request.POST.get('address_2', '')
        city = request.POST.get('city', '')
        state_or_province = request.POST.get('state_or_province', '')
        zip_code = request.POST.get('zip_code', '')
        country = request.POST.get('country', '')
        phone_number = request.POST.get('phone_number', '')
        depth_of_sori = request.POST.get('depth_of_sori', '')
        length_of_blade = request.POST.get('length_of_blade', '')
        type_of_steel = request.POST.get('type_of_steel', '')
        other_specifications = request.POST.get('other_specifications', '')

        messages = f"""
        Email: {email}
        Name: {name}
        Address 1: {address_1}
        Address 2: {address_2}
        City: {city}
        State or Province: {state_or_province}
        Zip Code: {zip_code}
        Country: {country}
        Phone Number: {phone_number}
        Depth of Sori: {depth_of_sori}
        Length of Blade: {length_of_blade}
        Type of Steel: {type_of_steel}
        Other Specifications: {other_specifications}
        """
        send_mail(
            'Sword order form', #email titel
            messages, # messages
            'settings.EMAIL_HOST_USER', #email for site
            ['brechkemmer01@gmail.com'], #email of recever
        fail_silently=False)
    return render(request, 'projects/order_form.html', )


def details_h(request, hotel_id):
    hotel_details = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'projects/details_h.html', {'hotel': hotel_details})


def sales(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)

        if form.is_valid():
            item_number = form.cleaned_data['item_number']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            city = form.cleaned_data['city']
            state_or_province = form.cleaned_data['state_or_province']
            zip_code = form.cleaned_data['zip_code']
            country = form.cleaned_data['country']
            phone_number = form.cleaned_data['phone_number']

            html = render_to_string('projects/emails/salesform.html', {
                'item_number': item_number,
                'email': email,
                'name': name,
                'address_1': address_1,
                'address_2': address_2,
                'city': city,
                'state_or_province': state_or_province,
                'zip_code': zip_code,
                'country': country,
                'phone_number': phone_number,

            })

            send_mail('order form for blade sales', 'this is the order',
                    ['brechkemmer01@gmail.com'], html_message=html)

            return redirect('sales')

    else:
        form = SalesForm()
    sword_sales = Sword_sales.objects
    return render(request, 'projects/sales.html', {'sword_sales': sword_sales, "form": form})


def details_sales(request, sword_sales_id):
    sword_sales_detail = get_object_or_404(Sword_sales, pk=sword_sales_id)
    return render(request, 'projects/details_sales.html', {'sword_sales_detailes': sword_sales_detail})
