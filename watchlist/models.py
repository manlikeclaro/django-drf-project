from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# def avg_rating(queryset, current_avg, current_count):
#     total_rating = current_avg * current_count
#     for item in queryset:
#         total_rating += item.rating
#     average = total_rating / current_count
#     return average

def avg_rating(queryset, current_count):
    total_rating = 0
    for item in queryset:
        total_rating += item.rating
    average = total_rating / current_count
    return average


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
    average_rating = models.FloatField(default=0, editable=False)
    total_reviews = models.IntegerField(default=0, editable=False)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, related_name="movies")
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save()
        elif self.reviews.count() > 0:
            queryset = Review.objects.filter(product=self.pk)
            # self.average_rating = avg_rating(queryset, self.average_rating, self.total_reviews)
            self.average_rating = avg_rating(queryset, self.total_reviews)
            self.total_reviews = self.reviews.count()
            super().save()

    def __str__(self):
        return f'Title: {self.title}'


class Review(models.Model):
    rating = models.FloatField(validators=(MinValueValidator(1.0), MaxValueValidator(10.0)))
    description = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.product.total_reviews = self.product.reviews.count() + 1
            self.product.save()
            super().save()

        self.product.total_reviews = self.product.reviews.count()
        super().save()
        self.product.save()

    def __str__(self):
        return f'Rating: {self.rating}'
