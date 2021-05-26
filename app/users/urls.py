from django.urls import path
from users.views import UserListCreateAPIView, UserDetailAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view()),
    path('<int:pk>/', UserDetailAPIView.as_view()),
]
