from django.test import TestCase
from api.models import Livestream
from django.contrib.auth.models import AnonymousUser, User
from django.db import IntegrityError

# Create your tests here.

class LivestreamTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='robzom', password='password')
        

    def test_user_follows_same_streamer_multiple_times(self):
        livestream1 = Livestream(user=self.user1, name='Forsen', twitchUsername='forsen')
        livestream2 = Livestream(user=self.user1, name='Forsen', twitchUsername='forsen')
        livestream1.save()
        with self.assertRaises(IntegrityError):
            livestream2.save()