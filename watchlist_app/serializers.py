from django.utils.translation import activate
from watchlist_app.models import Movie
from rest_framework import serializers, validators


def description_length(value):
    if len(value) < 5:
        raise serializers.ValidationError("Desc. is too short")


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(validators=[description_length])
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, data):  # Validate Object
        if data['name'] == data['description']:
            raise serializers.ValidationError('Should not be same')
        return data

    def validate_name(self, value):  # Validate Field
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value
