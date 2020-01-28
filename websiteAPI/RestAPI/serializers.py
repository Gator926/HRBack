from websiteAPI.RestAPI.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "phone", "department_id", "is_supervisor", "is_view_all")