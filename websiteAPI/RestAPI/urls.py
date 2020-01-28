from django.urls import path, include
from rest_framework import routers
from websiteAPI.RestAPI import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
