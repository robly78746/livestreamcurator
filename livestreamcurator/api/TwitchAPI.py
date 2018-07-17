import requests
import json
from django.conf import settings

# login limit is 100; fix this later
def usersInfo(usernames):
    if usernames is None or len(usernames) == 0:
        return []
    url = 'https://api.twitch.tv/helix/users?'
    userLogins = ['login=' + username for username in usernames]
    params = '&'.join(userLogins)
    url += params
    headers = {'Client-ID': settings.TWITCH_CLIENT_ID}
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    data = json_data['data']
    return data
    
# input: username
# output: boolean True if username is a valid Twitch username; False otherwise
def userValid(username):
    if username is None:
        return False
    return usersValid([username])[username]
    
# input: list of usernames
# output: dict of usernames as keys and boolean as values
def usersValid(usernames):
    if usernames is None or len(usernames) == 0:
        return {}
    data = usersInfo(usernames)
    userValidity = dict()
    for username in usernames:
        userValidity[username] = False
    for userInfo in data:
        userValidity[userInfo['login']] = True
    return userValidity
    
def userId(username):
    id = None
    userDict = userIds([username])
    if username in userDict:
        id = userDict[username]
    return id
    
def userIds(usernames):
    data = usersInfo(usernames)
    userIds = dict()
    for userInfo in data:
        userIds[userInfo['login']] = userInfo['id']
    return userIds
    
    
def streamsInfo(ids):
    if ids is None or len(ids) == 0:
        return []
    url = 'https://api.twitch.tv/helix/streams?'
    userIds = ['user_id=' + userId for userId in ids]
    params = '&'.join(userIds)
    url += params
    headers = {'Client-ID': settings.TWITCH_CLIENT_ID}
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    data = json_data['data']
    return data
    
# expects id
def userOnline(userId):
    if userId is None:
        return False
    return usersOnline([userId])[userId]
    
# will need user_id to match response to username, so will need to store user_id with livestream model
def usersOnline(userIds):
    if userIds is None or len(userIds) == 0:
        return {}
    data = streamsInfo(userIds)
    livestreams = dict()
    for userId in userIds:
        livestreams[userId] = False
    for streamInfo in data:
        userId = streamInfo['user_id']
        livestreams[userId] = streamInfo['type'] == 'live'  
    return livestreams