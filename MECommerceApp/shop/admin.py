from django.contrib import admin
from shop.models import products,Contact
# Register your models here.
admin.site.register(products)

class ProductAdmin(admin.ModelAdmin):
     list_display=['product_id','product_name','product_desc','pub_date','category','subcategory','price','image']


admin.site.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['msg-id','Usernmae','Email','Desc','Phone']