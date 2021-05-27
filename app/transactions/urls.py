from django.urls import path
from transactions.views import TransactionListCreateAPIView, TransactionDetailAPIView, TransactionSumView

urlpatterns = [
    path('', TransactionListCreateAPIView.as_view(), name='transactions'),
    path('<int:pk>/', TransactionDetailAPIView.as_view(), name='transaction'),
    path('sum/', TransactionSumView.as_view())
]
