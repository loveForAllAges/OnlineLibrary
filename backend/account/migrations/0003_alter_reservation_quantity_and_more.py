# Generated by Django 5.0 on 2023-12-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_reservation_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]