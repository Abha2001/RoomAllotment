# Generated by Django 2.1.11 on 2020-03-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomBooking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomNo', models.IntegerField()),
                ('IsEmpty', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]