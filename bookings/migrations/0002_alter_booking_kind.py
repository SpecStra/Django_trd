# Generated by Django 4.1.1 on 2022-09-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='kind',
            field=models.CharField(choices=[('room', 'Room'), ('experience', 'Experience')], max_length=15),
        ),
    ]
