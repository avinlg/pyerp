from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'url', 'username', 'email', 'groups']