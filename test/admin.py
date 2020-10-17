from django.contrib import admin
from test.models import *
# Register your models here.

admin.site.register(Token)
admin.site.register(user)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(Goods)

@admin.register(SubCategory)
class subCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','category')
    fieds = ('id','name','category')
    filter_horizontal = ('attributes',)


@admin.register(SubItem)
class subItemAdmin(admin.ModelAdmin):
    list_display = ('id','name','sub')
    fieds = ('id','name','sub')
