from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from accounts.api import views

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
