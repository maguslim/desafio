# Generated by Django 5.0.7 on 2024-08-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_userprofile_phone_number_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_locador',
            field=models.BooleanField(default=False),
        ),
    ]