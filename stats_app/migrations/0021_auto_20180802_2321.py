# Generated by Django 2.0.5 on 2018-08-03 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0020_auto_20180802_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gunshot',
            name='city_or_county',
            field=models.CharField(max_length=70),
        ),
    ]
