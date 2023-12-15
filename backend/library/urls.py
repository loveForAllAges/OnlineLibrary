from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [
    path('', include(router.urls)),
        
    path('download/<uuid:pk>/', DownloadAPIView.as_view(), name='download'),
    path('booking/<uuid:pk>/', BookingAPIView.as_view(), name='booking'),
]
