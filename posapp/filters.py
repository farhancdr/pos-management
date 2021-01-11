import django_filters 
from .models import Products

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['productName','productCode','productCost']