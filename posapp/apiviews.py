from django.core import serializers
# from django.utils import simplejson
from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework  import status
from .models import Sales
from .serializers import SalesSerializer


class add_sale_api(APIView):
    def get(self, request):
        
        salesobj = Sales.objects.all()
        serializer = SalesSerializer(salesobj,many = True)
        return Response(serializer.data)

    def post(self, request):
        pass