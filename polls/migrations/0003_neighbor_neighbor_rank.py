# Generated by Django 2.0.1 on 2018-01-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_target_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbor',
            name='neighbor_rank',
            field=models.IntegerField(default=-1),
        ),
    ]