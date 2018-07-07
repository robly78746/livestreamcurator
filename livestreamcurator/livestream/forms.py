from django import forms
from .models import Livestream, LivestreamGroup
from django.contrib.auth.models import User
from . import twitchAPI as TwitchAPI

class LivestreamForm(forms.ModelForm):
    class Meta:
        model = Livestream
        exclude = ['user', 'twitchUserId']
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
    #def clean_twitchUsername(self):
    #    cleaned_twitchUsername = self.cleaned_data['twitchUsername']
        
     #   if not TwitchAPI.userValid(cleaned_twitchUsername):
     #       raise forms.ValidationError('Twitch username not found.')
     #   return cleaned_twitchUsername
        
class LivestreamGroupForm(forms.ModelForm):
    class Meta:
        model = LivestreamGroup
        exclude = ['user']
        
    # verifies livestreamGroup form fields are unique to user
    # have to override because we don't ask for user in form which normally 
    # excludes user from validation
    def validate_unique(self):
        exclude = self._get_validation_exclusions()
        exclude.remove('user') # allow checking against the missing attribute

        try:
            self.instance.validate_unique(exclude=exclude)
        except forms.ValidationError as e:
            self._update_errors(e.message_dict)
