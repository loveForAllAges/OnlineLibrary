from django.db import models
from django.contrib.auth.models import AbstractUser

from library.models import Book


class User(AbstractUser):
    surname = models.CharField(max_length=128, blank=True)
    reservations = models.ManyToManyField(Book, through='Reservation')


RESERVATION_CHOICES = {
    'reserved': 'Забронировано',
    'started': 'Используется',
    'returned': 'Возвращено',
}


class Reservation(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
    )
    book = models.ForeignKey(
        Book, 
        on_delete=models.CASCADE, 
        related_name='reserverd'
    )
    status = models.CharField(max_length=32, choices=RESERVATION_CHOICES, default='reserverd')
    booking_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    return_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.created
