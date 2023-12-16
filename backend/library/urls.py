from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
# router.register(r'authors', AuthorListAPIView, basename='author')

# print(router.urls)
urlpatterns = [
    path('', include(router.urls)),
    path('authors/', AuthorListAPIView.as_view(), name='author-list'),
        
    path('download/<uuid:pk>', DownloadAPIView.as_view(), name='download'),
    path('booking/<uuid:pk>', BookingAPIView.as_view(), name='booking'),
]
