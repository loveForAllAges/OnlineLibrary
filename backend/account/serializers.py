from rest_framework.reverse import reverse
from rest_framework import serializers

from .models import User, Reservation
from library.models import Book


class ReservationSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='book-detail')
    booking = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ('url', 'booking')

    def get_booking(self, obj):
        data = None
        if not obj.is_digital:
            data = reverse(
                'booking',
                kwargs={'pk': obj.pk},
                request=self.context.get('request'),
            )
        return data


class UserSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        return super().update(instance, validated_data)    
