from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView

from .serializers import CategorySerializer

class Categories(APIView):
    serializer_class = CategorySerializer

    def get(self, request, format=None):
        return




