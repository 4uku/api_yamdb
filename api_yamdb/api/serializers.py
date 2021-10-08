from rest_framework import serializers
from rest_framework.fields import CharField, EmailField
from reviews.models import User


class CreateAndGetCode(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=150, min_length=3, allow_blank=False)
    email = serializers.EmailField(required=True, allow_blank=False, max_length=254)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Такой пользователь уже существует')
        return value
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Пользователь с таким email уже существует')
        return value

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, allow_blank=False, max_length=254)
    username = serializers.CharField(required=True, max_length=150, min_length=3, allow_blank=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('Такой пользователь уже зарегистрирован')
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Пользователь с таким email уже зарегистрирован')
        return data


class MeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=150, min_length=3, allow_blank=False)
    email = serializers.EmailField(required=True, allow_blank=False, max_length=254)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    bio = serializers.CharField(max_length=300)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=150, min_length=3, allow_blank=False)
    confirmation_code = serializers.CharField(required=True, min_length=5, allow_blank=False)
