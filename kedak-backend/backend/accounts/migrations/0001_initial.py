# Generated by Django 4.2.2 on 2023-08-15 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('business_name', models.CharField(blank=True, default='', max_length=255)),
                ('about', models.TextField(blank=True, default='')),
                ('country', models.CharField(blank=True, default='', max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('occupation', models.CharField(blank=True, default='', max_length=255)),
                ('phone_number', models.BigIntegerField(blank=True, default=None, null=True)),
                ('instagram_profile', models.CharField(blank=True, default='', max_length=100)),
                ('instagram_link', models.CharField(blank=True, default='', max_length=500)),
                ('twitter_profile', models.CharField(blank=True, default='', max_length=100)),
                ('twitter_link', models.CharField(blank=True, default='', max_length=500)),
                ('linkedin_profile', models.CharField(blank=True, default='', max_length=100)),
                ('linkedin_link', models.CharField(blank=True, default='', max_length=500)),
                ('tiktok_profile', models.CharField(blank=True, default='', max_length=100)),
                ('tiktok_link', models.CharField(blank=True, default='', max_length=100)),
                ('whatsapp_profile', models.CharField(blank=True, default='', max_length=100)),
                ('whatsapp_link', models.CharField(blank=True, default='', max_length=100)),
                ('youtube_profile', models.CharField(blank=True, default='', max_length=100)),
                ('youtube_link', models.CharField(blank=True, default='', max_length=100)),
                ('behance_profile', models.CharField(blank=True, default='', max_length=100)),
                ('behance_link', models.CharField(blank=True, default='', max_length=100)),
                ('facebook_profile', models.CharField(blank=True, default='', max_length=100)),
                ('facebook_link', models.CharField(blank=True, default='', max_length=500)),
                ('github_profile', models.CharField(blank=True, default='', max_length=100)),
                ('github_link', models.CharField(blank=True, default='', max_length=500)),
                ('snapchat_profile', models.CharField(blank=True, default='', max_length=100)),
                ('snapchat_link', models.CharField(blank=True, default='', max_length=500)),
                ('dribbble_profile', models.CharField(blank=True, default='', max_length=100)),
                ('dribbble_link', models.CharField(blank=True, default='', max_length=500)),
                ('website', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
