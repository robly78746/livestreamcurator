from rest_framework import serializers
from .models import Livestream
from django.contrib.auth.models import User
from . import TwitchAPI

from django.shortcuts import get_object_or_404

class LivestreamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Livestream
        fields = ('id', 'name', 'twitchUsername')
        depth = 1
        
    def create(self, validated_data):
        user = self.context['user']
        validated_data['user'] = user
        livestream = super(LivestreamSerializer, self).create(validated_data)
        return livestream
        
    def validate_twitchUsername(self, value):
        if not TwitchAPI.userValid(value):
            raise serializers.ValidationError("Invalid Twitch username")
        return value
            
    
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