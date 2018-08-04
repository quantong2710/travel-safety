# Generated by Django 2.0.5 on 2018-08-03 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats_app', '0019_auto_20180802_2311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gunshot',
            name='congressional_district',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='date',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='gun_stolen',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='gun_type',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='incident_characteristics',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='incident_url',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='incident_url_fields_missing',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='location_description',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='n_guns_involved',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='n_injured',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='n_killed',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='participant_age',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='participant_age_group',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='participant_gender',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='participant_name',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='participant_relationship',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='participant_status',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='participant_type',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='source_url',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='sources',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='state_house_district',
        ),
        migrations.RemoveField(
            model_name='gunshot',
            name='state_senate_district',
        ),
    ]
