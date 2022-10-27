from django.contrib import admin
from django.urls import path, include

"""Media and Static Imports"""
from django.conf import settings
from django.conf.urls.static import static

"""Swagger documentation Imports"""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

"""Swagger configuration for Documentation our API"""
schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Auditica API",
        default_version= "1.0.0",
        description="this api is created to music app"
    ),
    public=True
)

"""All Routes Integrated with swagger"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',
        include([
            path('users/', include(('apps.users.urls', 'users'), namespace='users')),
            path('categories/', include(('apps.categories.urls', 'categories'), namespace='categories')),
            path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
        ]) 
    )
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


