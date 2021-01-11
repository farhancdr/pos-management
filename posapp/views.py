from django.core import serializers
# from django.utils import simplejson
from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework  import status
from .models import Sales
from .serializers import SalesSerializer
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Sales,Products,Brands,Catagory,Salescount,Purchase,Customer,NewSales
from .forms import ProductsForm, BrandsForm, CatagoryForm, SignUpForm, PurchaseProductsForm, SalesForm
from .filters import OrderFilter

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'userform.html',{'form':form,'type':"Signup"})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'userform.html',{'form':form,'type':"Login"})

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')

@login_required(login_url='login')
def home(request):
    json_serializer = serializers.get_serializer("json")()
    current_user = request.user
    products = Products.objects.count()
    countme = json_serializer.serialize(Salescount.objects.all())
    return render(request,'home.html',{'User':current_user, 'products':products,'countme':countme})

#@login_required(login_url='login')
def add_product(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/') 
    context = {
        'form':form
    }
    return render(request,'add_form.html',context)


@login_required(login_url='login')
def update_product(request,pk):
    product = Products.objects.get(id=pk)
    form = ProductsForm(instance= product)
    if request.method == 'POST':
        form = ProductsForm(request.POST, instance= product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request,'add_form.html',context)

@login_required(login_url='login')
def delete_product(request,pk):
    product = Products.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')

    context={'item':product}
    return render(request,'delete.html',context)



@login_required(login_url='login')
def purchaseProduct(request):
    form = PurchaseProductsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/') 
    context = {
        'form':form
    }
    return render(request,'purchaseForm.html',context)



@login_required(login_url='login')
def updateproductCountList(request,pk):
    product = Purchase.objects.get(id=pk)
    form = PurchaseProductsForm(instance= product)
    if request.method == 'POST':
        form = PurchaseProductsForm(request.POST, instance= product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request,'purchaseForm.html',context)


@login_required(login_url='login')    
def productCountList(request):
    my_product_list = Purchase.objects.all()
    return render(request,'productCountList.html',{'Products':my_product_list})

def sales_list(request):
    my_sales_list = Sales.objects.all()
    return render(request,'salesList.html',{'Sales':my_sales_list})






@login_required(login_url='login')    
def product_list(request):
    my_product_list = Products.objects.all()
    myfilter = OrderFilter(request.GET, queryset = my_product_list)
    my_product_list = myfilter.qs
    return render(request,'product_list.html',{'Products':my_product_list,'Filters':myfilter})






@login_required(login_url='login')
def add_catagory(request):
    form = CatagoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_catagory')
    context ={
        'form':form
    }
    return render(request,'add_form.html',context)


@login_required(login_url='login')
def add_brand(request):
    form = BrandsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('add_brand')
    context ={
        'form':form
    }
    return render(request,'add_form.html',context)




@login_required(login_url='login')
def add_sale(request):
    my_product_list = Products.objects.all()
    customer = Customer.objects.all()

    context = {
        'products' : my_product_list,
        'customers' : customer
    }

    if request.method == 'POST':
        scustomerNameid = request.POST['selected_customer']
        scustomerName = Customer.objects.get(id=scustomerNameid)
        sproductNameid = request.POST['selected_product']
        sproductName = Products.objects.get(id=sproductNameid)
        sproductPrice = request.POST['productPrice']
        sproductUnit = request.POST['productUnit']
        sales_info = Sales(scustomerName = scustomerName, sproductName = sproductName, sproductPrice = sproductPrice, sproductUnit = sproductUnit)
        sales_info.save()
        # print(f'{productName},{customerName},{productPrice},{productUnit}')

    return render(request,'salesForm.html',context)





@login_required(login_url='login')    
def customer_list(request):
    my_customer_list = Customer.objects.all()
    return render(request,'customersList.html',{'Customers':my_customer_list})

@login_required(login_url='login')    
def customer_list(request):
    my_customer_list = Customer.objects.all()
    return render(request,'customersList.html',{'Customers':my_customer_list})

@login_required(login_url='login')
def show_product(request):
    my_product_list = Products.objects.all()
    context = {
        'products' : my_product_list,
    }
    return render(request,'show_product.html',context)

def myajax(request):
    return render(request,'myajax.html')

def sendajax(request):
    fname = request.GET.get('fname', None)
    lname = request.GET.get('lname', None)
    print(fname,lname)
    data = {
        'country' : f'Your name is {fname}'
    }
    return JsonResponse(data)


def sendOrder(request):
    totalCost = request.GET.get('totalCost', None)
    tdate = request.GET.get('tdate', None)
    tmonth = request.GET.get('tmonth', None)
    tyear = request.GET.get('tyear', None)
    new_sales_info = NewSales(totalCost = totalCost, tdate = tdate, tmonth = tmonth, tyear = tyear)
    new_sales_info.save()
    data = {
        "Strings" : "Success"
    }
    return JsonResponse(data)

def getDate(request):
    sales_list
    date:{
        "hello" : "hdke"
    }
    return JsonResponse(date)

def getchartData(request):
    context = {
        "j": 2105,
        "aj": 1234,
        "bj": 5412,
        "cj": 6325,
        "dj": 7458,
        "ej": 9856,
        "fj": 2514,
        "gj": 6253,
        "hj": 2013,
        "ij": 5012,
        "jj": 3621,
        "kj": 4128
        
    }
    return JsonResponse(context)