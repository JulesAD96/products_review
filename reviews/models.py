from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    url = models.TextField()

    def __str__(self) -> str:
        return self.name


class ProductSize(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='products')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class ProductSite(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
        related_name='sites', related_query_name='site')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, 
        related_name='sites', related_query_name='site')
    productsize = models.ForeignKey(ProductSize, on_delete=models.CASCADE, 
        related_name='sites', related_query_name='site')
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
        related_name='comments', related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
        related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name