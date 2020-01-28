from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from websiteAPI.RestAPI import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

router = routers.DefaultRouter()
router.register(r"department", views.DepartmentViewSet)

urlpatterns = [
    url(r'^$', schema_view),
    path('', include(router.urls))
]
