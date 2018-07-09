from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Livestream(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    twitchUsername = models.CharField(max_length=200)
    twitchUserId = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
    class Meta:
        unique_together = ['user', 'name']
        
class LivestreamGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    livestreams = models.ManyToManyField(Livestream)
    
    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ['user', 'name']
    