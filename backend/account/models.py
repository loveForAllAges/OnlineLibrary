from django.db import models
from django.contrib.auth.models import AbstractUser

from library.models import Book


class User(AbstractUser):
    reservations = models.ManyToManyField(Book, through='Reservation')


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
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.created
