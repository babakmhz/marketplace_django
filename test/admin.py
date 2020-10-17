from django.contrib import admin
from test.models import *
# Register your models here.

admin.site.register(Token)
admin.site.register(user)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(CategoryAttribute)
admin.site.register(SubCategory)
admin.site.register(Goods)