from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=30,blank=False,null=False)
    email = models.CharField(max_length=50,blank=False,null=False)

class Post(models.Model):
    comment = models.CharField(max_length=250,blank=False,null=False)
    users = models.ForeignKey(Customer,on_delete=models.CASCADE)
