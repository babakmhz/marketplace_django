from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.


class Token(models.Model):
    token = models.CharField(max_length=30)

# this code snippet i used for modeling users, althogh we could use djangorestframework toekn native lib


class user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.OneToOneField(Token, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class Attribute(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.name)


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,related_name='subCategories')

    attributes = models.ManyToManyField(Attribute, default='', blank=True)
    def __str__(self):
        return '{}'.format(self.name)


class SubItem(models.Model):
    name = models.CharField(max_length=30)
    sub = models.ForeignKey(SubCategory, on_delete=models.CASCADE,related_name='items')

    def __str__(self):
        return '{}'.format(self.name)


class Goods(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    sub = models.ForeignKey(SubItem, on_delete=models.SET_NULL, null=True,related_name='goods')
    image = models.ImageField(upload_to='images/goods',blank=True)
    discount = models.DecimalField(decimal_places=2, max_digits=2)

    def __str__(self):
        return '{}'.format(self.name)
