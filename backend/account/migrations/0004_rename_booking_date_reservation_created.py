# Generated by Django 5.0 on 2023-12-16 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_reservation_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='booking_date',
            new_name='created',
        ),
    ]