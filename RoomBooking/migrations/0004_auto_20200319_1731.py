# Generated by Django 2.1.11 on 2020-03-19 17:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RoomBooking', '0003_guest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='roomNo',
        ),
        migrations.AddField(
            model_name='guest',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='roomAllotted',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RoomBooking.Room'),
        ),
        migrations.AddField(
            model_name='guest',
            name='toTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='guest',
            name='fromTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomNo',
            field=models.IntegerField(unique=True),
        ),
    ]