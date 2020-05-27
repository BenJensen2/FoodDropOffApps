# Generated by Django 2.2.4 on 2020-05-27 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Location', '0001_initial'),
        ('RestaurantLogin', '0002_auto_20200526_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='name',
            new_name='restaurant_name',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='owner',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='Location.Location'),
            preserve_default=False,
        ),
    ]
