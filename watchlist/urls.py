from django.urls import path, include

from watchlist import views

urlpatterns = [
    path('movies', views.MoviesView.as_view(), name='movies'),
    path('movies/<int:movie_id>', views.SingleMovieView.as_view(), name='single-movie'),
]
