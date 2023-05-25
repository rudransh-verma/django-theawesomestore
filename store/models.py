from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100, default="")
    product_description = models.CharField(max_length=1000, default="")
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    published_date = models.DateField(default="")
    image = models.ImageField(upload_to="store/images", default="")


    def __str__(self):
        return self.product_name
