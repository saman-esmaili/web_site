from django.db import models

class Test(models.Model):
    full_name = models.CharField(max_length=20,blank=True,null=True)
    email = models.CharField(max_length=35)
    balance = models.IntegerField()

class relate(models.Model):
    date = models.DateField()
    test = models.ForeignKey(Test,on_delete=models.DO_NOTHING)

# Create your models here.
