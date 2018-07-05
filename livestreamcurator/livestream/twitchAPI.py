import requests
import json
from django.conf import settings

# input: username
# output: boolean True if username is a valid Twitch username; False otherwise
def userValid(username):
    return usersValid([username])[username]
    
# input: list of usernames
# output: dict of usernames as keys and boolean as values
def usersValid(usernames):
    url = 'https://api.twitch.tv/helix/users?'
    userLogins = ['login=' + username for username in usernames]
    params = '&'.join(userLogins)
    url += params
    headers = {'Client-ID': settings.TWITCH_CLIENT_ID}
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    data = json_data['data']
    usernameValidity = dict()
    for username in usernames:
        usernameValidity[username] = False
    for userInfo in data:
        usernameValidity[userInfo['login']] = True
    
    return usernameValidity
    
def userIds(usernames):
    url = 'https://api.twitch.tv/helix/users?'
    userLogins = ['login=' + username for username in usernames]
    params = '&'.join(userLogins)
    url += params
    headers = {'Client-ID': settings.TWITCH_CLIENT_ID}
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    data = json_data['data']
    userIds = dict()
    for userInfo in data:
        userIds[userInfo['id']] = userInfo['login']
    return userIds
    
def userOnline(username):
    return usersOnline([username])[username]
    
# will need user_id to match response to username, so will need to store user_id with livestream model
def usersOnline(usernames):
    userIdDict = userIds(usernames)
    validUsernames = userIdDict.values()
    url = 'https://api.twitch.tv/helix/streams?'
    userLogins = ['user_login=' + username for username in validUsernames]
    params = '&'.join(userLogins)
    url += params
    headers = {'Client-ID': settings.TWITCH_CLIENT_ID}
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    data = json_data['data']
    livestreams = dict()
    for username in usernames:
        livestreams[username] = False
    for streamInfo in data:
        username = userIdDict[streamInfo['user_id']]
        livestreams[username] = streamInfo['type'] == 'live'  
    return livestreams