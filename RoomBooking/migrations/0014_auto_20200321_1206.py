# Generated by Django 2.1.11 on 2020-03-21 12:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RoomBooking', '0013_auto_20200321_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.TimeField(default=datetime.time(0, 0))),
                ('endTime', models.TimeField(default=datetime.time(0, 0))),
                ('RoomNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RoomBooking.Room')),
            ],
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='fromDate',
            new_name='Date',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='fromTime',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='toDate',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='toTime',
        ),
        migrations.AlterField(
            model_name='guest',
            name='roomAllotted',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RoomBooking.Room'),
        ),
        migrations.AddField(
            model_name='guest',
            name='Time',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='RoomBooking.Available'),
        ),
    ]