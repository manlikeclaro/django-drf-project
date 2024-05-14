from django.urls import path

from watchlist.api import views

urlpatterns = [
    path('movies', views.MoviesView.as_view(), name='movies-list'),
    path('movies/<int:movie_id>', views.SingleMovieView.as_view(), name='movie-detail'),
]
