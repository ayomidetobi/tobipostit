from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets, ModelForm
from django.db import models
from .models import Post, Profile

class EditForm(UserChangeForm):
        username = forms.CharField()
        first_name = forms.CharField()
        last_name = forms.CharField()
        email = forms.EmailField()
        

        class Meta:
                model = User
                fields = ('username', 'first_name', 'last_name', 'email')

class UpdateProfileForm(forms.ModelForm):
        class Meta:
                model = Profile
                fields = ( 'Bio', 'What_i_Do')


class Post_form(forms.ModelForm):
        class Meta:
                model =Post
                fields= ('title','text', 'created_date')


