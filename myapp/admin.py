from django.contrib import admin
from myapp.models import Categrory,Product,User,Customer,Cart
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=["id","pname","pcat","price"]

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','cname','city','gender','email']

class UserAdmin(admin.ModelAdmin):
    list_display=['userid','uname','pwd','role']

class cartAdmin(admin.ModelAdmin):
    list_display=['customer','product','qty']

admin.site.register(Categrory)
admin.site.register(User,UserAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Cart,cartAdmin)
admin.site.register(Product,ProductAdmin)

