from users.models import CustomUser
from users.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.utils import UserFilterBackend

'''
Class for list and create users by anyone
'''


# TODO: Replace current access with the authorization system
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    filter_backends = (UserFilterBackend,)

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        order = self.request.query_params.get('order_by', None)

        if order:
            users = users.order_by(order)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


'''
Class for retrieve, update and destroy specific user by anyone
'''


# TODO: Replace current access with the authorization system
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
