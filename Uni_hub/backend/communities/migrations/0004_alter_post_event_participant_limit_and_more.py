# Generated by Django 5.2.1 on 2025-05-11 22:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_post_event_participant_limit_post_event_participants'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='event_participant_limit',
            field=models.PositiveIntegerField(blank=True, help_text='Maximum number of participants for this event', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='event_participants',
            field=models.ManyToManyField(blank=True, related_name='participated_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
