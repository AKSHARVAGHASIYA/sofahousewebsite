# models.py
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pic = models.FileField()
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.name

class Add_Cart(models.Model):
    p_id =models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pic = models.FileField()
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(default=1, decimal_places=2, max_digits=10)

class coupon(models.Model):
    code=models.CharField(max_length=6)
    discount = models.IntegerField()

class Billing(models.Model):
    c_countryname = models.CharField(max_length=50)
    c_fname = models.CharField(max_length=50)
    c_lname = models.CharField(max_length=50)
    c_companyname = models.CharField(max_length=50)
    c_address = models.CharField(max_length=100)
    c_full_address = models.CharField(max_length=150)
    c_state_country = models.CharField(max_length=50)
    c_email = models.EmailField()
    c_phone = models.IntegerField()