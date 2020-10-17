from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.

class Token(models.Model):
    token = models.CharField(max_length=30)

#this code snippet i used for modeling users, althogh we could use djangorestframework toekn native lib 
class user(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    token = models.OneToOneField(Token,on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=30)

class Attribute(models.Model):
    name = models.CharField(max_length=10)

class CategoryAttribute(models.Model):
    name = models.CharField(max_length=10)

class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    attributes = models.ManyToManyField(Attribute,default='',blank=True)

class Goods(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    attributes = models.ForeignKey(CategoryAttribute,on_delete=models.SET_NULL,null=True,default='')
    sub = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='images/goods')
    discount = models.DecimalField(decimal_places=2,max_digits=2)
