from django import forms




class ClassesForm(forms.Form):
    class_name = forms.CharField(max_length=25)
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    address_1 = forms.CharField(max_length=100)
    address_2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state_or_province = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=13)

STEEL_CHOICE =(
    (1, ("L6")),
    (2, ("1086")),
)

class OrderForm(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=100, required=True)
    address_1 = forms.CharField(max_length=100, required=True)
    address_2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100, required=True)
    state_or_province = forms.CharField(max_length=100, required=True)
    zip_code = forms.CharField(max_length=100, required=True)
    country = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=13, required=True)
    depth_of_sori = forms.IntegerField(max_value=1.25, required=True)
    length_of_blade = forms.IntegerField(max_value=32, required=True)
    type_of_steel = forms.ChoiceField(choices=STEEL_CHOICE, required=True)
    other_specifications = forms.ChoiceField(widget=forms.Textarea)

class SalesForm(forms.Form):
    item_number = forms.IntegerField()
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    address_1 = forms.CharField(max_length=100)
    address_2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state_or_province = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=13)
