# movies/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, TVShowViewSet, CombinedViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'tvshows', TVShowViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all/', CombinedViewSet.as_view({'get': 'all'})),
]
