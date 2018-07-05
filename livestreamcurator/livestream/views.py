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


# Create your views here.
def profile(request, username):
    user = request.user
    ownPage = user.is_authenticated and user.username == username
    pageUser = get_object_or_404(User, username=username)
    context = {'ownPage': ownPage, 'pageUser': pageUser}
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
        livestream = Livestream(user=request.user)
    else:
        # editing
        livestream = get_object_or_404(Livestream, user=request.user, name=streamer)
    if request.method == 'POST':
        form = LivestreamForm(request.POST, instance=livestream)
        if form.is_valid():
            form.save()
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
    group = get_object_or_404(LivestreamGroup, user=user, name=groupName)
    context = {'ownPage': ownPage, 'pageUser': pageUser, 'group': group}
    return render(request, 'livestream/group.html', context)
