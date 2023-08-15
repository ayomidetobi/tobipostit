from django.contrib import admin
from .models import UserAccount,UserProfile
# Register your models here.
myModels = [UserAccount,UserProfile]  # iterable list
admin.site.register(myModels)
