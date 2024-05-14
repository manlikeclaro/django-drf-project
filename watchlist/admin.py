from django.contrib import admin

from watchlist.models import Movie


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
