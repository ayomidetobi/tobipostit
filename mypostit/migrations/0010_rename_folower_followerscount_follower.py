# Generated by Django 4.1.1 on 2022-10-05 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypostit', '0009_followerscount_profile_following'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followerscount',
            old_name='folower',
            new_name='follower',
        ),
    ]
