from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('signup', SignupAPIView.as_view()),
    # path('users/<int:pk>/', UserAPIView.as_view(), name='user-detail'),
]
