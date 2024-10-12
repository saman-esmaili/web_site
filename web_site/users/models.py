from django.db import models


class Customer(models.Model):
    fullName = models.CharField(max_length=30,blank=False,null=False)
    email = models.CharField(max_length=50,blank=False,null=False)
    birthDate = models.CharField(max_length=50,blank=False,null=True)
    gender = models.CharField(max_length=10,blank=False,null=True)
    username = models.CharField(max_length=50,blank=False,null=True)
    password = models.CharField(max_length=500,blank=False,null=True)

class Post(models.Model):
    comment = models.CharField(max_length=250,blank=False,null=False)
    users = models.ForeignKey(Customer,on_delete=models.CASCADE)

class Products(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.CharField(max_length=35)
    amount = models.IntegerField(null=True)
