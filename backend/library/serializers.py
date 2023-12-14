from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='books-detail')
    download_url = serializers.SerializerMethodField()
    book_a_book = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_download_url(self, obj):
        data = None
        if obj.is_digital:
            data = reverse(
                'download', 
                kwargs={'pk': obj.pk}, 
                request=self.context.get('request'),
            )
        return data

    def get_book_a_book(self, obj):
        data = None
        if not obj.is_digital:
            data = reverse(
                'book-a-book',
                kwargs={'pk': obj.pk},
                request=self.context.get('request'),
            )
        return data
