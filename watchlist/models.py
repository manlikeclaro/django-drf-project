from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.id}'