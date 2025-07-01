from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(format = "%Y-%m-%d", input_formats=['%Y-%m-%dT', '%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%SZ'])
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_of_birth', 'phone_number']

class RegisterSerialize(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'date_of_birth', 'phone_number']
    def create(self, validated_data):
        user = Users.objects.create_superuser(**validated_data)
        return user

class LoginSerialize(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    class Meta:
        model = Users
        fields = ['username', 'password']