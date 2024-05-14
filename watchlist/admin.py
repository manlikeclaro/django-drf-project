from django.contrib import admin

from watchlist.models import Product, Platform


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active', 'created')


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'website')
