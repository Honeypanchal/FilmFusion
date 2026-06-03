# movies/serializers.py

from rest_framework import serializers
from .models import Movie, TVShow

class MovieSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_type(self, obj):
        return 'movie'

class TVShowSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = TVShow
        fields = '__all__'

    def get_type(self, obj):
        return 'tvshow'
