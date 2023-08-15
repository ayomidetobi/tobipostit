# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email,username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)

        user.set_password(password)
        user.save()

        return user
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255 ,unique=False)
    username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def profile(self):
        profile = UserProfile.objects.get(user=self)
        return profile
    
    def __str__(self):
        return self.email
class UserProfile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='profile')
    email=models.EmailField(max_length=255)
    username=models.CharField(max_length=255)
    business_name = models.CharField(max_length=255, default='', blank=True)
    about = models.TextField(default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    occupation = models.CharField(max_length=255, default='', blank=True)
    phone_number = models.BigIntegerField(default=None, blank=True,null=True)
    instagram_profile = models.CharField(max_length=100, blank=True, default='')
    instagram_link = models.CharField(max_length=500, blank=True, default='')
    twitter_profile = models.CharField(max_length=100, blank=True, default='')
    twitter_link = models.CharField(max_length=500, blank=True, default='')
    linkedin_profile = models.CharField(max_length=100, blank=True, default='')
    linkedin_link = models.CharField(max_length=500, blank=True, default='')
    tiktok_profile = models.CharField(max_length=100, blank=True, default='')
    tiktok_link = models.CharField(max_length=100, blank=True, default='')
    whatsapp_profile = models.CharField(max_length=100, blank=True, default='')
    whatsapp_link = models.CharField(max_length=100, blank=True, default='')
    youtube_profile = models.CharField(max_length=100, blank=True, default='')
    youtube_link = models.CharField(max_length=100, blank=True, default='')
    behance_profile = models.CharField(max_length=100, blank=True, default='')
    behance_link = models.CharField(max_length=100, blank=True, default='')
    facebook_profile = models.CharField(max_length=100, blank=True, default='')
    facebook_link = models.CharField(max_length=500, blank=True, default='')
    github_profile = models.CharField(max_length=100, blank=True, default='')
    github_link = models.CharField(max_length=500, blank=True, default='')
    snapchat_profile = models.CharField(max_length=100, blank=True, default='')
    snapchat_link = models.CharField(max_length=500, blank=True, default='')
    dribbble_profile = models.CharField(max_length=100, blank=True, default='')
    dribbble_link = models.CharField(max_length=500, blank=True, default='')
    website = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=UserAccount)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, _ = UserProfile.objects.get_or_create(user=instance)
    else:
        profile = instance.profile

    profile.email = instance.email
    profile.username = instance.username
    profile.save()
