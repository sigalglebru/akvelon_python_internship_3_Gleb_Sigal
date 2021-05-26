from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.filters import BaseFilterBackend
import coreapi

schema_view = get_schema_view(
   openapi.Info(
      title='Akvelon Payments REST API',
      default_version='v1',
      description='For Akvelon by Sigal Gleb',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


class CustomFilterBackend(BaseFilterBackend):
   def get_schema_fields(self, view):
      return [coreapi.Field(
         name='order_by',
         location='query',
         required=False,
         type='string'
      )]
