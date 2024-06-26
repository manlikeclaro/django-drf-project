from django.contrib import admin
from django.urls import path, include

from watchmate import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('watchlist/', include('watchlist.api.urls')),
    path('accounts/', include('accounts.api.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
