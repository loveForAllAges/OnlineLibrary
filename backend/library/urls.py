from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')


urlpatterns = [
    path('', include(router.urls)),
        
    path('download/<uuid:pk>/', DownloadAPIView.as_view(), name='download'),
    path('book-a-book/<uuid:pk>/', book_a_book, name='book-a-book'),
]
