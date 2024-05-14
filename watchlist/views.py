from django.http import JsonResponse
from django.views.generic import View

from watchlist.models import Movie


# Create your views here.
class MoviesView(View):
    movies = Movie.objects.all()

    def get(self, request):
        context = {
            "movies": list(self.movies.values())
        }
        return JsonResponse(context)


class SingleMovieView(View):
    movies = Movie.objects.all()

    def get(self, request, movie_id):
        single_movie = self.movies.get(pk=movie_id)
        context = {
            "id": single_movie.id,
            "name": single_movie.name,
            "description": single_movie.description,
            "status": single_movie.is_active,
        }
        return JsonResponse(context)
