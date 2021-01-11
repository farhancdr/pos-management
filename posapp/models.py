from django.db import models

class Brands(models.Model):
    brandName = models.CharField(max_length=50)
    def __str__(self):
        return self.brandName
class Catagory(models.Model):
    catagoryName = models.CharField(max_length=50)
    def __str__(self):
        return self.catagoryName
class Customer(models.Model):
    customerName = models.CharField(max_length=50)
    customerPhone = models.IntegerField(default=1)
    def __str__(self):
        return self.customerName
class Employee(models.Model):
    employeeName = models.CharField(max_length=50)
    def __str__(self):
        return self.employeeName
class Supplier(models.Model):
    supplierName = models.CharField(max_length=50)
    def __str__(self):
        return self.supplierName

class Products(models.Model):
    PRODUCT_TYPE_CHOICES = (
        ('Standard','Standard'),
        ('Normal','Normal')
    )
    productType = models.CharField(max_length=100,choices = PRODUCT_TYPE_CHOICES)
    productName = models.CharField(max_length=50)
    productCode = models.CharField(max_length=50)
    productBrand = models.ForeignKey(Brands,on_delete=models.CASCADE,default = 1)
    productCatagory = models.ForeignKey(Catagory,on_delete=models.CASCADE,default = 1)
    productCost = models.IntegerField()
    def __str__(self):
        return f'{self.productName}'


class Purchase(models.Model):
    sproductName = models.ForeignKey(Products,on_delete=models.CASCADE,default = None)
    supplierName = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    sproductUnit = models.IntegerField(default = None)
    sproductPrice = models.IntegerField(default = None)
    totalPrice = models.IntegerField(default = None)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.sproductName} : {self.sproductPrice}'


class Sales(models.Model):
    scustomerName = models.ForeignKey(Customer,on_delete=models.CASCADE,default = None)
    sproductName = models.ForeignKey(Products,on_delete=models.CASCADE,default = None)
    sproductUnit = models.IntegerField(default = None)
    sproductPrice = models.IntegerField(default = None)
    salesTime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.sproductName} : {self.sproductPrice} : {self.salesTime}'
class NewSales(models.Model):
    totalCost = models.IntegerField(default = None)
    tdate = models.IntegerField(default = None)
    tmonth = models.IntegerField(default = None)
    tyear = models.IntegerField(default = None)

    def __str__(self):
         return f'{self.totalCost} Year: {self.tyear}, Month: {self.tmonth}, Date: {self.tdate}'
class Salescount(models.Model):
    MONTHS = (
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December')
    )
    monthName = models.CharField(max_length=50,choices = MONTHS)
    howmuchsales = models.IntegerField()
    def __str__(self):
        return f'{self.monthName}:{self.howmuchsales}'
    