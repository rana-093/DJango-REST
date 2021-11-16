from django.db import models
from django.db.models import fields
from django.utils.translation import activate
from watchlist_app.models import WatchList, StreamPlatform
from rest_framework import serializers

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"

class WatchListSerializer(serializers.Serializer):

    class Meta:
        model = WatchList
        fiels = "__all__"

