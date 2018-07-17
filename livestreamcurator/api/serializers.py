from rest_framework import serializers
from .models import Livestream, TwitchInfo
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from . import TwitchAPI

class LivestreamSerializer(serializers.ModelSerializer):
    twitchUsername = serializers.CharField(write_only=True)
    
    class Meta:
        model = Livestream
        fields = ('id', 'name', 'twitchUsername', 'twitchInfo')
        read_only_fields = ('twitchInfo',)
        depth = 1
        
    def create(self, validated_data):
        username = validated_data.pop('twitchUsername')
        follower = get_object_or_404(User, pk=self.context['user_id'])
        livestream = super(LivestreamSerializer, self).create(validated_data)
        twitchInfo, created = TwitchInfo.objects.get_or_create(username=username)
        if created:
            twitchInfo.userId = TwitchAPI.userId(twitchUsername)
            twitchInfo.save()
        livestream.twitchInfo = twitchInfo
        livestream.followers.add(follower)
        livestream.save()
        return livestream
            
    
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