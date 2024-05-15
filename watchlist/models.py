from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return f'Streaming Platform: {self.name}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True, related_name="products")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Title: {self.title}'


class Review(models.Model):
    rating = models.FloatField(validators=(MinValueValidator(1.0), MaxValueValidator(10.0)))
    description = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='reviews')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Rating: {self.rating}'

