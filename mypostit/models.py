from urllib import request
from django.db import models
from django.conf import settings
from django.utils import timezone
from django import forms
from django.urls import reverse
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        Bio = models.TextField(max_length=40000,default='imagename here based on username')
        following = models.ManyToManyField(User, related_name='following', blank=True)
        What_i_Do = models.CharField(max_length=100 ,default='imagename here based on username')

        def __init__(self, *args, **kwargs):
             super (Profile, self).__init__(*args, **kwargs)

class Post(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        
        def __str__(self):
                return self.title
        def get_absolute_url(self):
                return reverse("index")

class FollowersCount(models.Model):
        follower = models.CharField(max_length=1000)
        user=  models.CharField(max_length=1000)
        
        def __str__(self):
                return self.user
        
