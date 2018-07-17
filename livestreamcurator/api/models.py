from django.db import models
from django.contrib.auth.models import User

# Create your models here.
        
class Livestream(models.Model):
    user = models.ForeignKey(User, related_name='livestreams', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    twitchUsername = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name
        

        
        