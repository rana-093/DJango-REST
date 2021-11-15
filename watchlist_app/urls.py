from django.contrib import admin
from django.urls import path, include
# from watchlist_app.views import movie_list, movie_details
from watchlist_app.views import MovieDetailAV, MovieListAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-details')
]
