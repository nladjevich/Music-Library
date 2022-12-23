from rest_framework import serializers
from .models import Songs

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        field = ['title', 'artist', 'album', 'release_date', 'genre']