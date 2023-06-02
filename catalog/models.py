from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products")
    short_info = models.TextField()
    full_info = models.TextField()
    price = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse("product",kwargs={"product_pk":self.pk})

class AdditionalOption(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
