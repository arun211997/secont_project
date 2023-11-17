from django.db import models

# Create your models here.
class Product(models.Model):
        productname=models.CharField(max_length=255,null=True)
        price=models.IntegerField()
        quantity=models.IntegerField()
        image=models.ImageField(upload_to="image/",null=True)


