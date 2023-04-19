from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=1000)
    published_date = models.DateField()
