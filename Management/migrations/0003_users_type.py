# Generated by Django 4.2.5 on 2023-11-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_rename_event_name_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='type',
            field=models.CharField(choices=[('Event Planner', 'Event Planner'), ('guest', 'guest')], default='customer', max_length=20),
        ),
    ]
