from rest_framework import serializers, pagination
from .models import Song

class SongSerializer(serializers.Serializer):
    class Meta():
        model = Song
        fields = (
            'id',
            'name',
            'image',
            'artist',
            'category',
            'reproductions',
            'song',
            'album',
        )
    

class SongPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100