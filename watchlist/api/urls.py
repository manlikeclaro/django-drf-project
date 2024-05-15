from django.urls import path

from watchlist.api import views

urlpatterns = [
    path('platforms', views.PlatformsView.as_view(), name='platforms-list'),
    path('platforms/<int:pk>', views.PlatformDetailView.as_view(), name='platform-detail'),

    path('products', views.ProductsView.as_view(), name='products-list'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    path('products/<int:product_id>/reviews', views.ProductReviewsView.as_view(), name='product-reviews'),
    path('products/<int:product_id>/create-review', views.CreateProductReviewView.as_view(), name='create-review'),
    path('products/reviews/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
]
