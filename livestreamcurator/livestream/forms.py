from django import forms
from .models import Livestream
from django.contrib.auth.models import User
import requests
import json
from django.conf import settings

class LivestreamForm(forms.ModelForm):
    class Meta:
        model = Livestream
        exclude = ['user']
        labels = {
            'twitchUsername': 'Twitch Username'
        }
        
    # verifies livestream form fields are unique to user
    # have to override because we don't ask for user in form which normally 
    # excludes user from validation
    def validate_unique(self):
        exclude = self._get_validation_exclusions()
        exclude.remove('user') # allow checking against the missing attribute

        try:
            self.instance.validate_unique(exclude=exclude)
        except forms.ValidationError as e:
            self._update_errors(e.message_dict)
            
    # verifies twitch username is valid
    def clean_twitchUsername(self):
        cleaned_twitchUsername = self.cleaned_data['twitchUsername']
        if not validTwitchUsername(cleaned_twitchUsername):
            raise forms.ValidationError('Twitch username not found.')
        return cleaned_twitchUsername
        
        
def validTwitchUsername(username):
    return username in validTwitchUsernames([username])
    
def validTwitchUsernames(usernames):
    url = 'https://api.twitch.tv/helix/users?'
    userLogins = ['login=' + username for username in usernames]
    params = '&'.join(userLogins)
    url += params
    headers = {'Client-ID': settings.TWITCH_CLIENT_ID}
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    data = json_data['data']
    validUsernames = [userInfo['login'] for userInfo in data]
    return validUsernames