from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import permissions, viewsets

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication, TokenAuthentication]