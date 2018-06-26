from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Livestream(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    twitchUsername = models.CharField(max_length=200)
    
    def __str__(self):
        return self.twitchUsername
        
    class Meta:
        unique_together = ['user', 'twitchUsername']