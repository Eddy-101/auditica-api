from django.shortcuts import render
from django.conf.urls import url

from rest_framework_swagger.views import get_swagger_view
from rest_framework.generics import ListAPIView

from .serializers import SongSerializer, SongPagination 
from .models import Song

# Create your views here.
class ListSongs(ListAPIView):
    serializer_class = SongSerializer
    pagination_class = SongPagination

    def get_queryset(self):
        return Song.objects.all()
    
    
