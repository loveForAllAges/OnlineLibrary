from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework import views, viewsets, permissions
from rest_framework.response import Response

from .serializers import BookSerializer, Book


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class DownloadAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(
            Book,
            pk=kwargs.get('pk'),
            attachment__isnull=False,
        )
        file_path = obj.attachment.path
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{obj.attachment.name}"'
        obj.downloaded += 1
        obj.save()
        return response


class BookingAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        message = 'Ошибка! Попробуйте еще раз!'
        obj = get_object_or_404(
            Book,
            pk=kwargs.get('pk'),
        )

        if request.user.reservations.filter(id=obj.id).exists():
            obj.quantity += 1
            request.user.reservations.remove(obj)
            message = 'Вы отменили бронь книги!'
        else:
            if obj.quantity > 0:
                obj.quantity -= 1
                request.user.reservations.add(obj)
                message = 'Вы забронировали книгу!'
            else:
                raise NotFound

        obj.save()

        return Response({'message': message})
