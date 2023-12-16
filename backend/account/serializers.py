from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Reservation
from .validators import validate_username
from library.models import Book


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[validate_username, UniqueValidator(User.objects.all(), 'Имя пользователя занято.')],
        error_messages={
            'blank': 'Это обязательное поле.',
        },
    )
    password = serializers.CharField(error_messages={
        'blank': 'Это обязательное поле.',
    })

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        instance = self.Meta.model.objects.create_user(**validated_data)
        return instance


class BookForReservationSerializer(serializers.HyperlinkedModelSerializer):
    unbooking = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ('url', 'unbooking', 'cover', 'title', 'description')

    def get_unbooking(self, obj):
        data = None
        if not obj.is_digital:
            data = reverse(
                'unbooking',
                kwargs={'pk': obj.pk},
                request=self.context.get('request'),
            )
        return data


class ReservationSerializer(serializers.ModelSerializer):
    book = BookForReservationSerializer()

    class Meta:
        model = Reservation
        fields = ('quantity', 'book')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    reservations = ReservationSerializer(many=True)

    class Meta:
        model = User
        fields = ('full_name', 'reservations')

    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password')
    #     instance.set_password(password)
    #     return super().update(instance, validated_data)    
