import requests
from django.core.management.base import BaseCommand
from movies.models import Movie, TVShow

TMDB_API_KEY = 'bcd9afc8b06f791ef291659f587aec16'
BASE_IMAGE_URL = "https://image.tmdb.org/t/p/"

class Command(BaseCommand):
    help = 'Fetch movies and TV shows from TMDB API and store them in the database'

    def handle(self, *args, **kwargs):
        self.fetch_and_save_movies()
        self.fetch_and_save_tvshows()

    def fetch_and_save_movies(self):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page=2'
        response = requests.get(url)

        if response.status_code == 200:
            movies = response.json().get('results', [])
            for movie_data in movies:
                self.save_movie(movie_data)
        else:
            self.stderr.write(f'Failed to fetch movies from TMDB. Status code: {response.status_code}')

    def fetch_and_save_tvshows(self):
        url = f'https://api.themoviedb.org/3/tv/popular?api_key={TMDB_API_KEY}&language=en-US&page=2'
        response = requests.get(url)

        if response.status_code == 200:
            tvshows = response.json().get('results', [])
            for tvshow_data in tvshows:
                self.save_tvshow(tvshow_data)
        else:
            self.stderr.write(f'Failed to fetch TV shows from TMDB. Status code: {response.status_code}')

    def save_movie(self, movie_data):
        tmdb_id = movie_data['id']
        title = movie_data['title']
        description = movie_data.get('overview', '')
        release_date = movie_data.get('release_date')
        rating = movie_data.get('vote_average')

        poster_path_w500 = f"{BASE_IMAGE_URL}w500{movie_data.get('poster_path', '')}"
        poster_path_original = f"{BASE_IMAGE_URL}original{movie_data.get('poster_path', '')}"
        backdrop_path_w500 = f"{BASE_IMAGE_URL}w500{movie_data.get('backdrop_path', '')}"
        backdrop_path_original = f"{BASE_IMAGE_URL}original{movie_data.get('backdrop_path', '')}"

        trailer_url = self.get_trailer_url(tmdb_id, 'movie')

        # Convert genre IDs to genre names
        genre_names = [self.get_genre_name(genre_id) for genre_id in movie_data.get('genre_ids', [])]
        genres = ', '.join(genre_names)

        movie, created = Movie.objects.update_or_create(
            tmdb_id=tmdb_id,
            defaults={
                'title': title,
                'description': description,
                'release_date': release_date,
                'rating': rating,
                'poster_path_w500': poster_path_w500,
                'poster_path_original': poster_path_original,
                'backdrop_path_w500': backdrop_path_w500,
                'backdrop_path_original': backdrop_path_original,
                'trailer_url': trailer_url,
                'genres': genres,  # Save genres as a comma-separated string
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Added movie: {title}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Updated movie: {title}'))

    def save_tvshow(self, tvshow_data):
        tmdb_id = tvshow_data['id']
        name = tvshow_data['name']
        description = tvshow_data.get('overview', '')
        first_air_date = tvshow_data.get('first_air_date')
        rating = tvshow_data.get('vote_average')

        poster_path_w500 = f"{BASE_IMAGE_URL}w500{tvshow_data.get('poster_path', '')}"
        poster_path_original = f"{BASE_IMAGE_URL}original{tvshow_data.get('poster_path', '')}"
        backdrop_path_w500 = f"{BASE_IMAGE_URL}w500{tvshow_data.get('backdrop_path', '')}"
        backdrop_path_original = f"{BASE_IMAGE_URL}original{tvshow_data.get('backdrop_path', '')}"

        trailer_url = self.get_trailer_url(tmdb_id, 'tv')

        # Convert genre IDs to genre names
        genre_names = [self.get_genre_name(genre_id) for genre_id in tvshow_data.get('genre_ids', [])]
        genres = ', '.join(genre_names)

        tvshow, created = TVShow.objects.update_or_create(
            tmdb_id=tmdb_id,
            defaults={
                'name': name,
                'description': description,
                'first_air_date': first_air_date,
                'rating': rating,
                'poster_path_w500': poster_path_w500,
                'poster_path_original': poster_path_original,
                'backdrop_path_w500': backdrop_path_w500,
                'backdrop_path_original': backdrop_path_original,
                'trailer_url': trailer_url,
                'genres': genres,  # Save genres as a comma-separated string
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Added TV show: {name}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Updated TV show: {name}'))

    def get_trailer_url(self, tmdb_id, media_type):
        url = f'https://api.themoviedb.org/3/{media_type}/{tmdb_id}/videos?api_key={TMDB_API_KEY}&language=en-US'
        response = requests.get(url)
        if response.status_code == 200:
            videos = response.json().get('results', [])
            for video in videos:
                if video['type'] == 'Trailer' and video['site'] == 'YouTube':
                    return f"https://www.youtube.com/watch?v={video['key']}"
        return None

    def get_genre_name(self, genre_id):
        genre_mapping = {
            28: 'Action',
            12: 'Adventure',
            16: 'Animation',
            35: 'Comedy',
            80: 'Crime',
            99: 'Documentary',
            18: 'Drama',
            10751: 'Family',
            14: 'Fantasy',
            36: 'History',
            27: 'Horror',
            10402: 'Music',
            9648: 'Mystery',
            10749: 'Romance',
            878: 'Science Fiction',
            10770: 'TV Movie',
            53: 'Thriller',
            10752: 'War',
            37: 'Western',
            10759: 'Action & Adventure',
            10762: 'Kids',
            10763: 'News',
            10764: 'Reality',
            10765: 'Sci-Fi & Fantasy',
            10766: 'Soap',
            10767: 'Talk',
            10768: 'War & Politics',
            37: 'Western',
        }
        return genre_mapping.get(genre_id, 'Unknown')
