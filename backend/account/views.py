from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics, views, permissions, status
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, SignupSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().prefetch_related('reservations')
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
