# Generated by Django 3.0.7 on 2020-06-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cau', '0006_room_electricity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room',
            field=models.IntegerField(default=0),
        ),
    ]
