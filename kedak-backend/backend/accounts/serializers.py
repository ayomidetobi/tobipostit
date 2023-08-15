from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import UserAccount,UserProfile
from django.contrib.auth import get_user_model
User = get_user_model()
class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model =UserProfile
        fields = '__all__'


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email', 'username', 'is_active', 'is_staff','profile')
        depth=1
