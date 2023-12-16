from django.db import models

import uuid


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.surname}'
    
    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.surname}'


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    quantity = models.PositiveSmallIntegerField(default=0)
    cover = models.ImageField(upload_to='images/covers/', null=True, blank=True)
    authors = models.ManyToManyField(Author)
    publication = models.DateField()

    is_digital = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='images/attachments/', null=True, blank=True)
    downloaded = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title[:20]
