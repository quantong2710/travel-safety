# Generated by Django 2.0.5 on 2018-07-15 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0003_auto_20180715_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gunshot',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
