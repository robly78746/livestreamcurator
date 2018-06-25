from django import forms
from .models import Livestream

class LivestreamForm(forms.ModelForm):
    class Meta:
        model = Livestream
        exclude = ['user']
        labels = {
            'twitchUsername': 'Twitch Username'
        }