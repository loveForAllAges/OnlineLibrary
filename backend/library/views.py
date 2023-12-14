from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.db.models import F

from rest_framework.decorators import api_view, permission_classes
# from rest_framework.exceptions import NotFound
from rest_framework import views, viewsets, permissions, status
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
            is_digital=True,
            attachment__isnull=False,
        )
        file_path = obj.attachment.path
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{obj.attachment.name}"'
        obj.downloaded += 1
        obj.save()
        return response


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def book_a_book(request, *args, **kwargs):
    obj = get_object_or_404(
        Book,
        pk=kwargs.get('pk'),
        is_digital=False,
        quantity__gt=0,
    )
    obj.quantity -= 1
    obj.save()
    # obj = Book.objects.filter(
    #     pk=kwargs.get('pk'), is_digital=False, quantity__gt=0
    # ).update(quantity=F('quantity') - 1)
    print(obj)
    return Response({'message': 'Вы забронировали книгу!'})
