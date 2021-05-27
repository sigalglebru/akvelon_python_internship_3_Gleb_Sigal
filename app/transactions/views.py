from django.db.models import Sum
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from transactions.utils import TransactionFilterBackend


'''
Class for list and create transactions by anyone
'''

# TODO: Replace current access with the authorization system
class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]
    filter_backends = (TransactionFilterBackend,)

    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.all()
        transaction_type = self.request.query_params.get('transaction_type', None)

        from_date = self.request.query_params.get('from_date', None)
        to_date = self.request.query_params.get('to_date', None)

        specific_user = self.request.query_params.get('specific_user', None)
        specific_date = self.request.query_params.get('specific_date', None)

        order = self.request.query_params.get('order_by', None)

        # Filter by transaction type from request
        if transaction_type:
            if transaction_type in ('out', 'in'):
                if transaction_type == 'in':
                    transactions = transactions.filter(amount__gt=0)
                else:
                    transactions = transactions.filter(amount__lt=0)

        # Set date range: from / to date, including date from request
        if from_date:
            transactions = transactions.filter(date__gte=from_date)

        if to_date:
            transactions = transactions.filter(date__lte=to_date)

        # Filter by specific user or date from request:
        if specific_user:
            transactions = transactions.filter(user=specific_user)

        if specific_date:
            transactions = transactions.filter(date=specific_date)

        # Sort final results as needed
        if order:
            transactions = transactions.order_by(order)

        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)


'''
Class for retrieve, update and destroy specific transaction by anyone
'''


# TODO: Replace current access with the authorization system
class TransactionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]


class TransactionSumView(APIView):
    permission_classes = [AllowAny]
    filter_backends = (TransactionFilterBackend,)

    def get(self, request) -> Response:
        from_date = request.query_params.get('from_date', None)
        to_date = request.query_params.get('to_date', None)
        transaction_type = self.request.query_params.get('transaction_type', None)

        specific_user = self.request.query_params.get('specific_user', None)
        specific_date = self.request.query_params.get('specific_date', None)

        order = self.request.query_params.get('order_by', None)
        transactions = Transaction.objects.filter().values('date').annotate(sum=Sum('amount'))

        # Filter by transaction type from request
        if transaction_type:
            if transaction_type in ('out', 'in'):
                if transaction_type == 'in':
                    transactions = Transaction.objects.filter(amount__gt=0).values('date').annotate(sum=Sum('amount'))
                else:
                    transactions = Transaction.objects.filter(amount__lt=0).values('date').annotate(sum=Sum('amount'))

        # Set date range: from / to date, including date from request
        if from_date:
            transactions = transactions.filter(date__gte=from_date)

        if to_date:
            transactions = transactions.filter(date__lte=to_date)

        # Filter by specific user or date from request:
        if specific_user:
            transactions = transactions.filter(user=specific_user)

        if specific_date:
            transactions = transactions.filter(date=specific_date)

        # Sort final results as needed
        if order:
            transactions = transactions.order_by(order)

        return Response(transactions)
