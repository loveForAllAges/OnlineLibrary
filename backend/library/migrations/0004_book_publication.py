# Generated by Django 5.0 on 2023-12-16 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_author_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication',
            field=models.DateField(default=datetime.date(2023, 12, 16)),
        ),
    ]