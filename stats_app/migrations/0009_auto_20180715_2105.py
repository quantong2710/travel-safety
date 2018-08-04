# Generated by Django 2.0.5 on 2018-07-16 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0008_auto_20180715_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gunshot',
            name='congressional_district',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gunshot',
            name='n_guns_involved',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gunshot',
            name='state_house_district',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gunshot',
            name='state_senate_district',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
