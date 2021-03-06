# Generated by Django 3.1.5 on 2021-01-09 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagoryName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=50)),
                ('customerPhone', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productType', models.CharField(choices=[('Standard', 'Standard'), ('Normal', 'Normal')], max_length=100)),
                ('productName', models.CharField(max_length=50)),
                ('productCode', models.CharField(max_length=50)),
                ('productCost', models.IntegerField()),
                ('productBrand', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posapp.brands')),
                ('productCatagory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posapp.catagory')),
            ],
        ),
        migrations.CreateModel(
            name='Salescount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthName', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=50)),
                ('howmuchsales', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplierName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sproductUnit', models.IntegerField(default=None)),
                ('sproductPrice', models.IntegerField(default=None)),
                ('salesTime', models.DateTimeField(auto_now_add=True)),
                ('scustomerName', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posapp.customer')),
                ('sproductName', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posapp.products')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sproductUnit', models.IntegerField(default=None)),
                ('sproductPrice', models.IntegerField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sproductName', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posapp.products')),
                ('supplierName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posapp.supplier')),
            ],
        ),
    ]
