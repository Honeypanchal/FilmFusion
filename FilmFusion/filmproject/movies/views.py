from rest_framework import viewsets
from .models import Movie, TVShow
from .serializers import MovieSerializer, TVShowSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TVShowViewSet(viewsets.ModelViewSet):
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer

# Additional combined view for both
class CombinedViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def all(self, request):
        movies = Movie.objects.all()
        tvshows = TVShow.objects.all()
        movie_serializer = MovieSerializer(movies, many=True)
        tvshow_serializer = TVShowSerializer(tvshows, many=True)
        return Response(movie_serializer.data + tvshow_serializer.data)
