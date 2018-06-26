from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.conf import settings
from .models import Livestream
from .forms import LivestreamForm


# Create your views here.
def profile(request, username):
    user = request.user
    ownPage = user.is_authenticated and user.username == username
    pageUser = get_object_or_404(User, username=username)
    context = {'ownPage': ownPage, 'pageUser': pageUser}
    return render(request, 'livestream/profile.html', context)
    
@login_required
def addStream(request, username):
    # check if post request or get request
    # process form if post
    authorized = request.user.username == username
    if not authorized:
        raise PermissionDenied
    if request.method == 'POST':
        livestream = Livestream(user=request.user)
        form = LivestreamForm(request.POST, instance=livestream)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('livestream:profile', args=(request.user.username,)))
    else:
        form = LivestreamForm()
        
    return render(request, 'livestream/add.html', {'form': form})
    
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
    

        
