from django.urls import path

from watchlist.api import views

urlpatterns = [
    path('products', views.ProductsView.as_view(), name='products-list'),
    path('products/<int:product_id>', views.ProductDetailView.as_view(), name='product-detail'),

    path('platforms', views.PlatformsView.as_view(), name='platforms-list'),
    path('platforms/<int:platform_id>', views.PlatformDetailView.as_view(), name='platform-detail'),
]
