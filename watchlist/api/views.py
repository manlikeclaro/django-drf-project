from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist.api.serializers import MovieSerializer, MovieModelSerializer
from watchlist.models import Movie


class MoviesView(APIView):
    movies = Movie.objects.all()

    def get(self, request):
        # serializer = MovieSerializer(self.movies, many=True)
        serializer = MovieModelSerializer(self.movies, many=True)
        return Response(serializer.data, 200, )

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400, )

        serializer.save()
        return Response(serializer.data, 201, )


class SingleMovieView(APIView):
    movies = Movie.objects.all()

    def get(self, request, movie_id):
        serializer = MovieSerializer(self.movies.get(pk=movie_id))
        return Response(serializer.data, 200, )

    def put(self, request, movie_id):
        movie = self.movies.get(pk=movie_id)
        serializer = MovieSerializer(movie, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400, )

        serializer.save()
        return Response(serializer.data, 201, )

    def delete(self, request, movie_id):
        movie = self.movies.get(pk=movie_id)
        movie.delete()
        return Response(status=204)
