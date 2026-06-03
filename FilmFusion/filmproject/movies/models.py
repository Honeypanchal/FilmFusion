from django.db import models

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    poster_path_w500 = models.CharField(max_length=255, null=True, blank=True)
    poster_path_original = models.CharField(max_length=255, null=True, blank=True)
    backdrop_path_w500 = models.CharField(max_length=255, null=True, blank=True)
    backdrop_path_original = models.CharField(max_length=255, null=True, blank=True)
    trailer_url = models.URLField(max_length=255, null=True, blank=True)  # New trailer field
    genres = models.CharField(max_length=255, null=True, blank=True)  # New genres field as comma-separated values

    def __str__(self):
        return self.title

class TVShow(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    first_air_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    poster_path_w500 = models.CharField(max_length=255, null=True, blank=True)
    poster_path_original = models.CharField(max_length=255, null=True, blank=True)
    backdrop_path_w500 = models.CharField(max_length=255, null=True, blank=True)
    backdrop_path_original = models.CharField(max_length=255, null=True, blank=True)
    trailer_url = models.URLField(max_length=255, null=True, blank=True)  # New trailer field
    genres = models.CharField(max_length=255, null=True, blank=True)  # New genres field as comma-separated values

    def __str__(self):
        return self.name
