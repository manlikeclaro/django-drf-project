from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from watchlist.api import views

urlpatterns = [
    path('', views.APIRootView.as_view(), name='api-root'),

    path('platforms/', views.PlatformsView.as_view(), name='platforms-list'),
    path('platforms/<int:pk>/', views.PlatformDetailView.as_view(), name='platform-detail'),

    path('products/', views.ProductsView.as_view(), name='products-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    path('products/<int:product_id>/reviews/', views.ProductReviewsView.as_view(), name='product-reviews'),
    path('products/<int:product_id>/create-review/', views.CreateProductReviewView.as_view(), name='create-review'),

    path('reviews/', views.UserReview.as_view(), name='user-reviews'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
