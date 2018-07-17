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
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # create user with user and password
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLivestreams(APIView):
    # get list of streamers that a user follows
    def get(self, request, user_id, format=None):
        livestreams = Livestream.objects.filter(user__id=user_id)
        serializer = LivestreamSerializer(livestreams, many=True)
        return Response(serializer.data)
    
class UserFollowStream(APIView):
    permission_classes = (IsAuthenticated,)
    
    # follows a livestreamer (copy livestream object for user_id)
    def put(self, request, user_id, livestream_id, format=None):
        authorized = request.user.id == user_id # logged in user is same as user whose follows are being edited
        if authorized:
            livestreamer = get_object_or_404(Livestream, id=livestream_id)
            try:
                # find out whether user is following a livestream with same name; if so, update
                livestreamerWithName = Livestream.objects.get(name=livestreamer.name, user__id=user_id)
                serializer = LivestreamSerializer(livestreamerWithName, data=livestreamer.__dict__, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Livestream.DoesNotExist:
                # else add livestreamer directly by nulling pk and saving
                livestreamer.pk = None
                livestreamer.user = request.user
                livestreamer.save()
                serializer = LivestreamSerializer(livestreamer)
                return Response(serializer.data)
            
        return Response(status=status.HTTP_403_FORBIDDEN)
    def delete(self, request, user_id, livestream_id, format=None):
        authorized = request.user.id == user_id # logged in user is same as user whose follows are being edited
        if authorized:
            livestreamer = get_object_or_404(Livestream, id=livestream_id, user__id=user_id)
            livestreamer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
class Livestreams(APIView):
    permission_classes = (IsAuthenticated,)
    # creates a livestreamer and has user follow
    def post(self, request, format=None):
        # if user follows streamer with given name already, then return all streamers with that name
        if 'name' in request.data:
            try:
                livestreamer = Livestream.objects.get(name=request.data['name'],user__id=request.user.id)
                serializer = LivestreamSerializer(livestreamer, data=request.data, partial=True)
            except Livestream.DoesNotExist:
                serializer = LivestreamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    # get list of livestreams user follows
    #def get(self, request, format=None):
    def put(self, request, livestream_id, format=None):
        livestreamer = get_object_or_404(Livestream, id=livestream_id, user__id=request.user.id)
        serializer = LivestreamSerializer(livestreamer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)