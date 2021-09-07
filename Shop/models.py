from django.db import models
from django.db.models.fields import DateField
# Create your models here.

class Product(models.Model):
    product_ID = models.AutoField(primary_key = True)
    product_Name = models.CharField(max_length = 30)
    product_price = models.FloatField(default = 0)
    product_desc = models.CharField(max_length = 300)
   # product_pic = models.ImageField(upload_to = 'media/', default = "")
    product_Qty = models.IntegerField(default = 1 )
    product_creation_time = models.DateField(null= False, auto_now_add = False)

    def __str__(self):
        return self.product_Name

class SearchHistory(models.Model):
    SearchContent = models.CharField(max_length=100)
    SearchTime = models.DateTimeField(null= False, auto_now_add=True)
    SearchHit = models.IntegerField(default=1)

    def __str__(self):
        return self.SearchContent
