from django.http import FileResponse
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter
from rest_framework.exceptions import NotFound
from rest_framework import views, viewsets, permissions, generics
from rest_framework.response import Response

from .serializers import BookSerializer, AuthorSerializer, Book, Author
from .filters import BookFilter

from account.models import Reservation


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend, SearchFilter, )
    filterset_class = BookFilter
    search_fields = (
        'title', 
        'description', 
        'authors__first_name', 
        'authors__last_name', 
        'publication'
    )
    serializer_class = BookSerializer
    queryset = Book.objects.all().prefetch_related('authors')


class DownloadAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(
            Book,
            pk=kwargs.get('pk'),
            attachment__isnull=False,
        )
        file_path = obj.attachment.path
        # TODO ЗАКРЫТИЕ ФАЙЛА ПОСЛЕ ОТКРЫТИЯ
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{obj.attachment.name}"'
        obj.downloaded += 1
        obj.save()
        return response


class BookingAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(
            Book,
            pk=kwargs.get('pk'),
            is_digital=False,
        )
        if obj.quantity > 0:
            reservation, created = Reservation.objects.get_or_create( 
                user=request.user,
                book=obj,
                status='reserved'
            )
            reservation.quantity += 1
            reservation.save()
            obj.quantity -= 1
            obj.save()
        else:
            raise NotFound        

        return Response({'message': 'Вы забронировали книгу!'})


class UnBookingAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(
            Book,
            pk=kwargs.get('pk'),
            is_digital=False,
        )
        reservation, created = Reservation.objects.get_or_create( 
            user=request.user,
            book=obj,
            status='reserved'
        )
        reservation.quantity -= 1
        reservation.delete() if reservation.quantity == 0 else reservation.save()
        obj.quantity += 1
        obj.save()

        return Response({'message': 'Вы отменили бронирование книги!'})
