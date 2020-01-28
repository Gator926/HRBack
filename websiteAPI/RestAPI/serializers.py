from websiteAPI.RestAPI.models import User, Department
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "phone", "department_id", "is_supervisor", "is_view_all")
