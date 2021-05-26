from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from akvelon_payments.yasg import CustomFilterBackend

class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]
    filter_backends = (CustomFilterBackend,)

    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.all()
        order = self.request.query_params.get('order_by', None)

        if order:
            transactions = transactions.order_by(order)

        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)


class TransactionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]
