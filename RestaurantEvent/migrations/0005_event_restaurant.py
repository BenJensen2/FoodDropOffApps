# Generated by Django 2.2.4 on 2020-05-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantLogin', '0001_initial'),
        ('RestaurantEvent', '0004_event_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='restaurant',
            field=models.ManyToManyField(related_name='events', to='RestaurantLogin.Restaurant'),
        ),
    ]
