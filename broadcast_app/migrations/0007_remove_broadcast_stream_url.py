# Generated by Django 5.2 on 2025-04-13 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broadcast_app', '0006_alter_profile_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='broadcast',
            name='stream_url',
        ),
    ]
