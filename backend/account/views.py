from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics, views, permissions, status, viewsets
from rest_framework.response import Response

from .models import User, Reservation
from .serializers import UserSerializer, SignupSerializer
from library.models import Book

from django.db.models import Prefetch


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().prefetch_related(
        Prefetch('reservations', queryset=Reservation.objects.prefetch_related(
            Prefetch('book', queryset=Book.objects.all())
        ))
    )
    serializer_class = UserSerializer


class LoginAPIView(ObtainAuthToken):
    permission_classes = []


class LogoutAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'message': 'Вы вышли из системы.'}, status=status.HTTP_200_OK)


class SignupAPIView(views.APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
