# Generated by Django 2.0.1 on 2018-01-19 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apogee_nn', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbor',
            old_name='sdss_link',
            new_name='SDSS_link',
        ),
    ]
