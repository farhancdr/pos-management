from django.urls import path,include
from rest_framework import routers
from . import views,apiviews



urlpatterns = [
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.home,name='home'),
    path('add_product',views.add_product,name='add_product'),
    path('update_product/<str:pk>/',views.update_product,name='update_product'),
    path('delete_product/<str:pk>/',views.delete_product,name='delete_product'),
    path('product_list',views.product_list,name='product_list'),
    path('purchaseProduct',views.purchaseProduct,name='purchaseProduct'),
    path('productCountList',views.productCountList,name='productCountList'),
    path('updateproductCountList/<str:pk>/',views.updateproductCountList,name='updateproductCountList'),
    path('add_catagory',views.add_catagory,name='add_catagory'),
    path('add_brand',views.add_brand,name='add_brand'),
    path('add_sale',views.add_sale,name='add_sale'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('add_supplier',views.add_supplier,name='add_supplier'),
    path('sales_list',views.sales_list,name='sales_list'),
    path('new_sales_list',views.new_sales_list,name='new_sales_list'),
    path('customer_list',views.customer_list,name='customer_list'),
    path('show_product',views.show_product,name='show_product'),
    path('myajax',views.myajax,name='myajax'),
    path('sendajax',views.sendajax,name='sendajax'),
    path('sendOrder',views.sendOrder,name='sendOrder'),
    path('getchartData',views.getchartData,name='getchartData'),

    # path('add_sale_api/',apiviews.add_sale_api.as_view(),name='add_sale_api')
]