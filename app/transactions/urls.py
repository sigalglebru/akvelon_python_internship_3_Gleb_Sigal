from django.urls import path
from transactions.views import TransactionListCreateAPIView, TransactionDetailAPIView, TransactionSumView

urlpatterns = [
    path('', TransactionListCreateAPIView.as_view()),
    path('<int:pk>/', TransactionDetailAPIView.as_view()),
    path('sum/', TransactionSumView.as_view())
]
