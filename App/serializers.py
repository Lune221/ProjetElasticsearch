from rest_framework import serializers

from .models import Film

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'plot', 'type', 'image_url', 'rank', 'year')