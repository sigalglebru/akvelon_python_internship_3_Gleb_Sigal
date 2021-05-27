from rest_framework import serializers
from users.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}
