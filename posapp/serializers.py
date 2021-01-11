from rest_framework import serializers
from .models import Sales


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['scustomerName','sproductName','sproductUnit','sproductPrice']