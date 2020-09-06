from django.db import models


# Create your models here.
class products(models.Model):
    prouct_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=2000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50, default="")
    Email = models.CharField(max_length=70, default="")
    Desc = models.CharField(max_length=2000, default="")
    Phone = models.CharField(max_length=10, default="")


    def __str__(self):
     return self.Username
