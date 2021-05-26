from users.models import CustomUser
from users.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from akvelon_payments.yasg import CustomFilterBackend

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    filter_backends = (CustomFilterBackend,)

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        order = self.request.query_params.get('order_by', None)

        if order:
            users = users.order_by(order)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
