from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.conf import settings
from .models import Livestream, LivestreamGroup
from .forms import LivestreamForm, LivestreamGroupForm
from . import twitchAPI as TwitchAPI


# Create your views here.

# split livestreams into live and offline
# output: live and offline usernames
def liveAndOfflineStreams(livestreams):
    if livestreams is None or livestreams.count() == 0:
        return [], []
    livestreamLookup = dict()
    for livestream in livestreams:
        livestreamLookup[livestream.twitchUserId] = livestream
    userIds = [stream.twitchUserId for stream in livestreams]
    streamStatuses = TwitchAPI.usersOnline(userIds)
    liveStreams = []
    offlineStreams = []
    for userId in streamStatuses:
        live = streamStatuses[userId]
        stream = livestreamLookup[userId]
        if live:
            liveStreams.append(stream)
        else:
            offlineStreams.append(stream)
    return liveStreams, offlineStreams
    
def liveAndOfflineGroups(groups, liveStreams):
    liveGroups = set()
    for livestream in liveStreams:
        for group in livestream.livestreamgroup_set.all():
            liveGroups.add(group)
            
    offlineGroups = []
    for group in groups:
        if group not in liveGroups:
            offlineGroups.append(group)
            
    liveGroups = list(liveGroups)
    return liveGroups, offlineGroups
        
        
def home(request):
    if request.user.is_authenticated:
        return profile(request, request.user.username)
    else:
        return render(request, 'livestream/home.html')
    
# need live and offline group
def profile(request, username):
    user = request.user
    ownPage = user.is_authenticated and user.username == username
    pageUser = get_object_or_404(User.objects.prefetch_related('livestream_set', 'livestreamgroup_set'), username=username)
    livestreams = pageUser.livestream_set.all().prefetch_related('livestreamgroup_set')
    groups = pageUser.livestreamgroup_set.all()
    live, offline = liveAndOfflineStreams(livestreams)
    liveGroups, offlineGroups = liveAndOfflineGroups(groups, live)
    context = {'ownPage': ownPage, 'pageUser': pageUser, 'live': live, 'offline': offline, 'liveGroups': liveGroups, 'offlineGroups': offlineGroups}
    return render(request, 'livestream/profile.html', context)
    
@login_required
def modifyStream(request, username, streamer=None):
    # check if post request or get request
    # process form if post
    authorized = request.user.username == username
    if not authorized:
        raise PermissionDenied
    if streamer is None:
        # adding
        # retrieve twitchId
        
        livestream = Livestream(user=request.user)
    else:
        # editing
        livestream = get_object_or_404(Livestream, user=request.user, name=streamer)
    if request.method == 'POST':
        form = LivestreamForm(request.POST, instance=livestream)
        
        if form.is_valid():
            livestream = form.save(commit=False)
            if streamer is None:
                userId = TwitchAPI.userId(livestream.twitchUsername)
                if userId is None:
                    raise Http404('Could not find Twitch user id from username')
                livestream.twitchUserId = userId
            livestream.save()
            return HttpResponseRedirect(reverse('livestream:profile', args=(request.user.username,)))
    else:
        form = LivestreamForm(instance=livestream)
        
    return render(request, 'livestream/modifyStream.html', {'form': form, 'add': streamer is None})
    
@login_required
@require_http_methods(['POST'])
def deleteStream(request, username):
    authorized = request.user.username == username
    if not authorized:
        raise PermissionDenied
    if 'id' in request.POST:
        livestream = get_object_or_404(Livestream, pk=request.POST['id'])
        livestream.delete()
    return HttpResponseRedirect(reverse('livestream:profile', args=(request.user.username,)))
    
@login_required
def modifyGroup(request, username, groupName=None):
    authorized = request.user.username == username
    if not authorized:
        raise PermissionDenied
    if groupName is None:
        # adding
        livestreamGroup = LivestreamGroup(user=request.user)
    else:
        # editing
        livestreamGroup = get_object_or_404(LivestreamGroup, user=request.user, name=groupName)
    if request.method == 'POST':
        form = LivestreamGroupForm(request.POST, instance=livestreamGroup)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('livestream:profile', args=(request.user.username,)))
    else:
        form = LivestreamGroupForm(instance=livestreamGroup)    
        
    return render(request, 'livestream/modifyGroup.html', {'form': form, 'add': groupName is None})

@login_required
@require_http_methods(['POST'])
def deleteGroup(request, username):
    authorized = request.user.username == username
    if not authorized:
        raise PermissionDenied
    if 'id' in request.POST:
        livestreamGroup = get_object_or_404(LivestreamGroup, pk=request.POST['id'])
        livestreamGroup.delete()
    return HttpResponseRedirect(reverse('livestream:profile', args=(request.user.username,)))
  
@login_required
@require_http_methods(['POST'])  
def deleteFromGroup(request, username, groupName):
    authorized = request.user.username == username
    if not authorized:
        raise PermissionDenied
    if 'id' in request.POST:
        livestream = get_object_or_404(Livestream, pk=request.POST['id'])
        livestreamGroup = get_object_or_404(LivestreamGroup, user=request.user, name=groupName)
        livestreamGroup.livestreams.remove(livestream)
    return HttpResponseRedirect(reverse('livestream:group_show', args=(request.user.username,groupName,)))
    
def showGroup(request, username, groupName):
    user = request.user
    ownPage = user.is_authenticated and user.username == username
    pageUser = get_object_or_404(User, username=username)
    group = get_object_or_404(LivestreamGroup, user=pageUser, name=groupName)
    context = {'ownPage': ownPage, 'pageUser': pageUser, 'group': group}
    return render(request, 'livestream/group.html', context)
