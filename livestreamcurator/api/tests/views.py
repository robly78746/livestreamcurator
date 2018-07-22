from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Livestream
from rest_framework.authtoken.models import Token

class UsersTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='robzom', password='password')
        self.user2 = User.objects.create_user(username='rob1', password='password')
        self.url = reverse('api:users')
        
    def test_get_user_info(self):
        username = 'robzom'
        params = {'username':username}
        response = self.client.get(self.url, params, format='json')
        data = response.data
        userInfo = data['results'][0]
        self.assertTrue(type(userInfo['id']) is int)
        self.assertEqual(userInfo['username'], username)
        
    def test_get_multiple_users_info(self):
        usernames = ['robzom', 'rob1']
        params = {'username':','.join(usernames)}
        response = self.client.get(self.url, params, format='json')
        userInfo1, userInfo2 = response.data['results']
        self.assertTrue(userInfo1['username'] in usernames and userInfo2['username'] in usernames)
        self.assertTrue(userInfo1['username'] != userInfo2['username'])
        self.assertTrue(userInfo1['id'] != userInfo2['id'])
        
    def test_get_user_no_usernames(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(len(response.data['results']), 2)
        
    def test_get_user_invalid_and_valid_usernames(self):
        usernames = ['robzom', 'what']
        params = {'username':','.join(usernames)}
        response = self.client.get(self.url, params, format='json')
        data = response.data['results'][0]
        self.assertTrue(type(data['id']) is int)
        self.assertEqual(data['username'], 'robzom')
        
    def test_get_user_one_page(self):
        username = 'robzom'
        params = {'username':username}
        response = self.client.get(self.url, params, format='json')
        data = response.data
        # next, previous, results
        self.assertEqual(data['previous'], None)
        self.assertEqual(data['next'], None)
        self.assertEqual(data['results'][0]['username'], username)
        
    def test_get_user_two_pages(self):
        # create 99 more users to make 2 pages necessary
        baseUsername = 'robTest'
        for i in range(99):
            User.objects.create_user(username=baseUsername + str(i), password='password')
        response = self.client.get(self.url, format='json')
        self.assertEqual(len(response.data['results']), 100)
        
        nextPageUrl = response.data['next']
        response2 = self.client.get(nextPageUrl, format='json')
        self.assertEqual(len(response2.data['results']), 1)
        
    def test_create_user(self):
        newUsername = 'newUser'
        bodyParams = {'username': newUsername, 'password': 'password'}
        self.client.post(self.url, bodyParams, format='json')
        users = User.objects.all()
        self.assertEqual(users.count(), 3)
        newUser = users.filter(username=newUsername)
        self.assertEqual(newUser.count(), 1)

    def test_create_user_missing_field(self):
        newUsername = 'newUser'
        bodyParams = {'username': newUsername}
        response = self.client.post(self.url, bodyParams, format='json')
        users = User.objects.all()
        self.assertEqual(users.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class UserLivestreamsTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='robzom', password='password')
        self.streamerName = 'Forsen'
        self.twitchUsername = 'forsen'
        self.livestream1 = Livestream.objects.create(user=self.user1, name=self.streamerName, twitchUsername=self.twitchUsername)
        self.urlTag = 'api:user_livestreams'
        self.token = Token.objects.create(user=self.user1)
        self.token.save()
        
    def test_list_livestreamers(self):
        url = reverse(self.urlTag, args=(self.user1.id,))
        response = self.client.get(url, format='json')
        data = response.data['results']
        self.assertEqual(len(data), 1)
        self.assertEqual(len(data[0]), 3)
        livestreamerInfo = data[0]
        self.assertTrue(type(livestreamerInfo['id']) is int)
        self.assertEqual(livestreamerInfo['name'], self.streamerName)
        self.assertEqual(livestreamerInfo['twitchUsername'], self.twitchUsername)
        
    def test_list_invalid_user_livestreams(self):
        url = reverse(self.urlTag, args=(0,))
        response = self.client.get(url, format='json')
        data = response.data['results']
        self.assertEqual(len(data), 0)
        
    def test_list_livestreamers_one_page(self):
        url = reverse(self.urlTag, args=(self.user1.id,))
        response = self.client.get(url, format='json')
        data = response.data
        self.assertEqual(data['previous'], None)
        self.assertEqual(data['next'], None)
        self.assertEqual(len(data['results']), 1)
        
    def test_list_livestreamers_two_pages(self):
        # create 99 more users to make 2 pages necessary
        baseUsername = 'robTest'
        for i in range(100):
            Livestream.objects.create(user=self.user1, name=self.streamerName + str(i), twitchUsername=self.twitchUsername)
        url = reverse(self.urlTag, args=(self.user1.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data['results']), 100)
        
        nextPageUrl = response.data['next']
        response2 = self.client.get(nextPageUrl, format='json')
        self.assertEqual(len(response2.data['results']), 1)
        
    def test_create_livestreamer(self):
        url = reverse(self.urlTag, args=(self.user1.id,))
        name = 'Kers55'
        twitchUsername = 'kers55'
        params = {'name':name,'twitchUsername':twitchUsername}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, params, format='json')
        data = response.data
        self.assertTrue(type(data['id']) is int)
        self.assertEqual(data['name'], name)
        self.assertEqual(data['twitchUsername'], twitchUsername)
        queryset = Livestream.objects.filter(name=name, twitchUsername=twitchUsername)
        self.assertEqual(queryset.count(), 1)
    
    def test_create_livestreamer_unauthenticated(self):
        url = reverse(self.urlTag, args=(self.user1.id,))
        name = 'Kers55'
        twitchUsername = 'kers55'
        params = {'name':name,'twitchUsername':twitchUsername}
        response = self.client.post(url, params, format='json')
        data = response.data
        queryset = Livestream.objects.filter(name=name, twitchUsername=twitchUsername)
        self.assertFalse(queryset.exists())
        
    def test_create_livestreamer_invalid_username(self):
        url = reverse(self.urlTag, args=(self.user1.id,))
        name = 'Kers55'
        twitchUsername = 'alskdjasdjlaskd'
        params = {'name':name,'twitchUsername':twitchUsername}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, params, format='json')
        data = response.data
        queryset = Livestream.objects.filter(name=name, twitchUsername=twitchUsername)
        self.assertFalse(queryset.exists())
        
    def test_create_livestreamer_duplicate_name(self):
        url = reverse(self.urlTag, args=(self.user1.id,))
        name = 'Forsen'
        twitchUsername = 'kers55'
        params = {'name':name,'twitchUsername':twitchUsername}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, params, format='json')
        queryset = Livestream.objects.filter(name=name)
        self.assertEqual(queryset.count(), 1)
        
class LivestreamerTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='robzom', password='password')
        self.streamerName = 'Forsen'
        self.twitchUsername = 'forsen'
        self.livestream1 = Livestream.objects.create(user=self.user1, name=self.streamerName, twitchUsername=self.twitchUsername)
        self.urlTag = 'api:update_livestream'
        self.token = Token.objects.create(user=self.user1)
        self.token.save()
        
    def test_retrieve_livestreamer(self):
        url = reverse(self.urlTag, args=(self.livestream1.id,))
        response = self.client.get(url, format='json')
        livestreamInfo = response.data
        self.assertEqual(livestreamInfo['id'], self.livestream1.id)
        self.assertEqual(livestreamInfo['name'], self.streamerName)
        self.assertEqual(livestreamInfo['twitchUsername'], self.twitchUsername)
        
    def test_update_livestream(self):
        url = reverse(self.urlTag, args=(self.livestream1.id,))
        newName = 'Nani'
        newUsername = 'nani'
        params = {'name': newName, 'twitchUsername': newUsername}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.client.put(url, params, format='json')
        updatedLivestream = Livestream.objects.get(pk=self.livestream1.id)
        self.assertEqual(updatedLivestream.name, newName)
        self.assertEqual(updatedLivestream.twitchUsername, newUsername)
        
    def test_delete_livestream(self):
        url = reverse(self.urlTag, args=(self.livestream1.id,))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.client.delete(url, format='json')
        livestreams = Livestream.objects.all()
        self.assertFalse(livestreams.exists())