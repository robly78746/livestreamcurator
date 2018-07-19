from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.test import APITestCase

class UsersTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='robzom', password='password')
        self.user2 = User.objects.create_user(username='rob1', password='password')
        self.url = reverse('api:users')
        
    def test_get_user_info(self):
        username = 'robzom'
        params = {'username':username}
        response = self.client.get(self.url, params, format='json')
        userInfo = response.data['results'][0]
        self.assertEqual(len(userInfo), 2)
        self.assertTrue(type(userInfo['id']) is int)
        self.assertEqual(userInfo['username'], username)
        
    def test_get_multiple_users_info(self):
        usernames = ['robzom', 'rob1']
        params = {'username':','.join(usernames)}
        response = self.client.get(self.url, params, format='json')
        self.assertEqual(len(response.data), 3)
        userInfo1, userInfo2 = response.data['results']
        self.assertTrue(userInfo1['username'] in usernames and userInfo2['username'] in usernames)
        self.assertTrue(userInfo1['username'] != userInfo2['username'])
        self.assertTrue(userInfo1['id'] != userInfo2['id'])
        
    def test_no_usernames(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(len(response.data), 3)
        self.assertEqual(len(response.data['results']), 2)
        
    def test_get_invalid_username(self):
        usernames = ['robzom', 'what']
        params = {'username':','.join(usernames)}
        response = self.client.get(self.url, params, format='json')
        self.assertEqual(len(response.data), 3)
        data = response.data['results'][0]
        self.assertEqual(len(data), 2)
        self.assertTrue(type(data['id']) is int)
        self.assertEqual(data['username'], 'robzom')