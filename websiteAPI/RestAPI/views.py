from websiteAPI.RestAPI.models import User
from rest_framework import viewsets
from websiteAPI.RestAPI.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
