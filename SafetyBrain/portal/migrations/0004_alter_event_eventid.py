# Generated by Django 4.1 on 2022-08-21 23:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_alter_event_eventid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventID',
            field=models.CharField(default=uuid.UUID('1c927ade-15a7-44ee-a79c-3c125ba42855'), max_length=50, null=True),
        ),
    ]