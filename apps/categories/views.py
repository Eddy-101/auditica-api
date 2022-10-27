from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.generics import ListAPIView

from .serializers import CategorySerializer
from .models import Category

class ListCategories(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()



