from django.db import models


# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True, related_name="products")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Title: {self.title}'
