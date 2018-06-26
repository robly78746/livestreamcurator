from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms import UserForm

# Create your views here.
def signup(request):
    # check if post request or get request
    # process form if post
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username = user.username, password = password)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect(reverse('livestream:home'))
    else:
        form = UserForm()
        
    return render(request, 'registration/signup.html', {'form': form})