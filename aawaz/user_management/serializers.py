from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import UserProfile
import jwt

class UpdateUserProfile(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('mobile_number', 'profile_image', 'user','cover_image','date_of_birth','gender','about','hometown','lavel','age', 'user')
# Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
    user_detail = UpdateUserProfile(read_only = True)
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username","user_detail",]


# Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=False,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    password = serializers.CharField(
        write_only=True, required=False, validators=[validate_password], default="[mR]h{?fTh3syV")
    password2 = serializers.CharField(write_only=True, required=False,  default="[mR]h{?fTh3syV")

    # password = "[mR]h{?fTh3syV"
    # password2 = "[mR]h{?fTh3syV"

    class Meta:
        model = User
        fields = ('username', 'password', 'password2' )
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            # email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
        )

        #user.set_password(validated_data['password'])
        user.set_password("[mR]h{?fTh3syV")
        UserProfile.objects.create(mobile_number=validated_data['username'], user= user)
        user.save()
        return user




