from django.contrib import admin
from django.urls import path, include

from watchmate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('watchlist/', include('watchlist.api.urls')),
]
