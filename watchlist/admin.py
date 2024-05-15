from django.contrib import admin

from watchlist.models import Product, Platform, Review


# Register your models here.
@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'website',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active', 'platform')
    readonly_fields = ('created',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating',)
    readonly_fields = ('created_on', 'updated_on')
