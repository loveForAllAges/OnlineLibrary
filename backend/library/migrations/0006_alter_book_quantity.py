# Generated by Django 5.0 on 2023-12-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
