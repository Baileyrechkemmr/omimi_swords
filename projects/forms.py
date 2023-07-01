from django import forms

STEEL_CHOICE =(
    ("L6"),
    ("1086"),
)


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

class OrderForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    address_1 = forms.CharField(max_length=100)
    address_2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state_or_province = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=13)
    depth_of_sori = forms.IntegerField(max_length=1.25)
    type_of_steel = forms.ChoiceField(choices=STEEL_CHOICE)
    length_of_blade = forms.IntegerField(max_length=32)
    other_specifications = forms.ChoiceField(widget=forms.Textarea)

class SalesForm(forms.Form):
    Item_Number = forms.IntegerField()
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    address_1 = forms.CharField(max_length=100)
    address_2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state_or_province = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=13)
