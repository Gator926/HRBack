from websiteAPI.RestAPI.models import User, Department
from rest_framework import viewsets
from websiteAPI.RestAPI.serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
