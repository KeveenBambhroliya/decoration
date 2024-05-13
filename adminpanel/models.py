
from django.db import models




# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Gallery(models.Model):
    type = models.CharField(max_length=100)
    date = models.DateField( auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to='Gallery_Images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

class Decoration(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Decoration_Images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    details = models.TextField()
    

