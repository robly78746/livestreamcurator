from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Livestream
from .serializers import LivestreamSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Users(APIView):
    # get list of user id and username from list of usernames
    def get(self, request, format=None):
        if 'username' in request.query_params:
            usernames = request.query_params['username'].split(',')
            usersByUsernames = User.objects.filter(username__in=usernames)
            serializer = UserSerializer(usersByUsernames, many=True)
            return Response(serializer.data)
        return Response([])
    
    # create user with user and password
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLivestreams(APIView):
    def get(self, request, user_id, format=None):
        user = get_object_or_404(User.objects.all().prefetch_related('livestream_set'), pk=user_id)
        livestreams = user.livestream_set.all()
        serializer = LivestreamSerializer(livestreams, many=True)
        return Response(serializer.data)
    
class UserFollowStream(APIView):
    def put(self, request, user_id, livestream_id, format=None):
        return
    def delete(self, request, user_id, livestream_id, format=None):
        return
    
class Livestreams(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        # if user follows streamer with given name already, then return all streamers with that name
        user = get_object_or_404(User.objects.all().prefetch_related('livestream_set'), pk=request.user.id)
        name = request.data['name']
        followedStreamers = user.livestream_set.filter(name=name)
        if followedStreamers.exists():
            serializer = LivestreamSerializer(followedStreamers, many=True)
        else:
            serializer = LivestreamSerializer(data=request.data, context={'user_id': user.id})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # get list of livestreams user follows
    #def get(self, request, format=None):
        
            
    
def modify_livestream(request, livestream_id):
    return