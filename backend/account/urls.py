from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('<int:pk>', UserAPIView.as_view(), name='user-detail'),
]
