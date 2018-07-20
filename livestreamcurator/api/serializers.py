from rest_framework import serializers
from .models import Livestream
from django.contrib.auth.models import User
from . import TwitchAPI

from django.shortcuts import get_object_or_404

class LivestreamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Livestream
        fields = ('id', 'name', 'twitchUsername')
        
    def validate_twitchUsername(self, value):
        if not TwitchAPI.userValid(value):
            raise serializers.ValidationError("Invalid Twitch username")
        return value
    
    def update(self, instance, validated_data):
        instance.user = self.context.get('user', instance.user)
        instance.name = validated_data.get('name', instance.name)
        instance.twitchUsername = validated_data.get('twitchUsername', instance.twitchUsername)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user