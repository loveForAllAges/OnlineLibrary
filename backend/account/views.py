from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().prefetch_related('reservations')
    serializer_class = UserSerializer
