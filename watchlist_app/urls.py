from django.contrib import admin
from django.urls import path, include
from watchlist_app.views import WatchListAV, WatchListDetailAV, StreamPlatformAV
from watchlist_app.views import StreamPlatformDetailAV

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/',WatchListDetailAV.as_view(),name='movie-details'),
    
    path('stream/',StreamPlatformAV.as_view(),name='stream'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-detail')
]