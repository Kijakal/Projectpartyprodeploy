# Generated by Django 4.2.5 on 2023-11-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0003_users_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='type',
            field=models.CharField(choices=[('Event Planner', 'Event Planner'), ('Guest', 'Guest')], default='customer', max_length=20),
        ),
    ]
