from django.db.models import fields
from django.utils.translation import activate
from watchlist_app.models import Movie
from rest_framework import serializers, validators


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_len_name(self, object):
        length = len(object.name)
        return length
