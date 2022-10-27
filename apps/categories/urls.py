from django.urls import path
from .views import (
    ListCategories,
)

urlpatterns = [
    path('', ListCategories.as_view())
]
