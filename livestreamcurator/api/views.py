from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Livestream
from .serializers import LivestreamSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.serializers import ValidationError

from rest_framework import mixins
from rest_framework import generics

# Create your views here.

class Users(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    ordering_fields = 'id'
    
    def get_queryset(self):
        # returns users with usernames in comma delimited list in query parameter 'username' 
        queryset = User.objects.all()
        usernames = self.request.query_params.get('username', None)
        if usernames is not None:
            usernames = usernames.split(',')
            queryset = queryset.filter(username__in=usernames)
        return queryset
    

class UserLivestreams(generics.ListCreateAPIView):
    # get list of streamers that a user follows
    serializer_class = LivestreamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        queryset = Livestream.objects.all()
        user_id = self.kwargs.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user__id=user_id)
        return queryset
        
    # check if user already follows a livestreamer with name
    def perform_create(self, serializer):
        livestreamerName = serializer.validated_data['name']
        user = self.request.user
        queryset = Livestream.objects.filter(name__iexact=livestreamerName, user=user)
        if queryset.exists():
            raise ValidationError('User is already following a livestreamer with that name.')
        serializer.save(user=user)
    
class Livestreamer(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = LivestreamSerializer
    queryset = Livestream.objects.all()
    