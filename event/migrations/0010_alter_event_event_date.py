# Generated by Django 3.2.6 on 2021-08-27 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_alter_event_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date & Time...(YYYY-MM-DD)'),
        ),
    ]