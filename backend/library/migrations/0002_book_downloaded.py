# Generated by Django 5.0 on 2023-12-14 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='downloaded',
            field=models.PositiveIntegerField(default=0),
        ),
    ]