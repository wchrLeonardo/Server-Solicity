from rest_framework import serializers
from .models import UserService

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserService
        fields = ['id', 'nome', 'email', 'senha']
        extra_kwargs = {'senha': {'write_only': True}}
        
        def create(self, validated_data):
            user = UserService.objects.create_user(
                nome=validated_data['nome'],
                email=validated_data['email'],
                senha=validated_data['senha']
            )
            return user
        
