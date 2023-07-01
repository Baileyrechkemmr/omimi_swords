from django import forms


class ClassesForm(forms.Form):
    class_type = forms.CharField(max_length=25)
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    address_1 = forms.CharField(max_length=100)
    address_2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state_or_province = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=13)
