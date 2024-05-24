from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


def avg_rating(queryset, current_count):
    total_rating = 0
    for item in queryset:
        total_rating += item.rating
    average = total_rating / current_count
    return average


def calc_avg_rating(queryset):
    # Use Django's Avg aggregation function to calculate the average rating
    average_rating = queryset.aggregate(avg_rating=Avg('rating'))['avg_rating']
    return average_rating or 0  # Handle None if no ratings are present


# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)
    total_movies = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Checking if the object is being created
        if not self.pk:
            super().save()

        else:
            movies_count = self.movies.count()
            count_changed = False

            old_count = Platform.objects.get(pk=self.pk).total_movies
            if old_count != movies_count:
                count_changed = True

            if count_changed:
                self.total_movies = movies_count
                super().save()

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    average_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0, editable=False)
    total_reviews = models.IntegerField(default=0, editable=False)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, related_name="movies")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Save the new product instance
            super().save(*args, **kwargs)
            if self.platform is not None:
                self.platform.save()

        else:
            review_count = self.reviews.count()

            # If the product has reviews
            if review_count > 0:
                # Get all reviews related to this product
                queryset = Review.objects.filter(product=self.pk)

                # Calculate the new average rating with the current total reviews
                self.average_rating = avg_rating(queryset, review_count)
                # self.average_rating = calc_avg_rating(queryset, )

                # Update the total number of reviews
                self.total_reviews = review_count

            # Save the product instance
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    rating = models.FloatField(validators=(MinValueValidator(1.0), MaxValueValidator(10.0)))
    description = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        rating_changed = False
        is_new = not self.pk

        if not is_new:
            # Fetch the old rating if the review already exists
            old_rating = Review.objects.get(pk=self.pk).rating
            if old_rating != self.rating:
                rating_changed = True

        # Save the review instance
        super().save(*args, **kwargs)

        # If the rating has changed, update the product's average rating and total reviews
        if rating_changed or is_new:
            self.product.save()

    def delete(self, *args, **kwargs):
        # Delete the Review instance
        super().delete(*args, **kwargs)

        # Save the updated Product instance
        self.product.save()

    class Meta:
        unique_together = ('product', 'author')

    def __str__(self):
        return f'Rating: {self.rating}'
