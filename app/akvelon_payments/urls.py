from django.contrib import admin
from django.urls import path, include
import users.urls
from .yasg import urlpatterns as doc_urls

api_urls = [
    path('users/', include(users.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls))
]

urlpatterns += doc_urls