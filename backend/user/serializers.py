from django.db.models import fields
from rest_framework import serializers
from .models import User,Login


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'password',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined', 
            'is_chef', 
            'is_bartender', 
            'is_purchaser', 
            'is_service', 
            'is_owner', 
            'birth_day', 
            'is_working', 
            'gender', 
            'img',
            'is_banned'
        ]


class LoginSerializer(serializers.ModelSerializer):
    user_set = UserSerializer(read_only=True,source="user")
    class Meta:
        model = Login
        fields = ['id','token','user','login_at','logout_at','time_login','user_set'] 