from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TwitchInfo(models.Model):
    username = models.CharField(max_length=200, unique=True)
    userId = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username
        
class Livestream(models.Model):
    followers = models.ManyToManyField(User)
    name = models.CharField(max_length=200)
    twitchInfo = models.ForeignKey(TwitchInfo, related_name='livestreams', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.name
        

        
        