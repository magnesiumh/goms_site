# Generated by Django 3.1.7 on 2021-09-07 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='Event_details',
        ),
        migrations.AlterField(
            model_name='event',
            name='Event_Name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='event',
            name='Venue',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
