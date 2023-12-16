from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'full_name')


class AuthorsForBookSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ('full_name', 'url')

    def get_url(self, obj):
        return reverse(
            'book-list',
            request=self.context.get('request'),
        )


class BookSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='book-detail')
    download_url = serializers.SerializerMethodField()
    authors = AuthorsForBookSerializer(many=True, read_only=True)
    booking = serializers.SerializerMethodField()
    downloaded = serializers.IntegerField(max_value=9223372036854775807, min_value=0, read_only=True)

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

    def get_booking(self, obj):
        data = None
        if not obj.is_digital:
            data = reverse(
                'booking',
                kwargs={'pk': obj.pk},
                request=self.context.get('request'),
            )
        return data
