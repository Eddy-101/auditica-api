from django.urls import path

"""View Imports"""
from .views import (
    ListUsers,
)


urlpatterns = [
    path('', ListUsers.as_view())
]