# Generated by Django 2.0.5 on 2018-08-03 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0018_auto_20180802_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
