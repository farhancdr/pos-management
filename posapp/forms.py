from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Products,Brands,Catagory,Sales,Purchase



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2', )


    
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'productName',
            'productCode',
            'productBrand',
            'productCatagory',
            'productCost'
        ]

class PurchaseProductsForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [
            'sproductName',
            'supplierName',
            'sproductUnit',
            'sproductPrice',
            'totalPrice'
            ]




class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = [
            'brandName',
        ]
class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = [
            'catagoryName',
        ]


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = [
            'sproductName',
            'sproductUnit',
            'sproductPrice',
            'scustomerName'
        ]