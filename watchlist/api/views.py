from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist.api.serializers import MovieSerializer
from watchlist.models import Movie


class MoviesView(APIView):
    movies = Movie.objects.all()

    def get(self, request):
        serializer = MovieSerializer(self.movies, many=True)
        return Response(serializer.data, 200, )


class SingleMovieView(APIView):
    movies = Movie.objects.all()

    def get(self, request, movie_id):
        serializer = MovieSerializer(self.movies.get(pk=movie_id))
        return Response(serializer.data, 200, )
