# Livestream Curator

This web application lets users manage and share the live streamers they follow across platforms. With the rise in popularity of live streaming, more live streaming platforms have become available for both streamers and viewers. This site aims to serve as a central hub for live stream viewers.

## User Stories

- Viewer watches a streamer on Twitch. Twitch streamer gets temporarily banned and streams on YouTube for a while. The viewer wants to know which platform the streamer is using. The viewer adds the streamer along with the streamer's Twitch and YouTube channels. The website checks which is live and shows the link to the live stream.

- A viewer watches some streamers that stream on Twitch and some that stream on YouTube. The viewer would like to know which streamers are online. The viewer browses to their profile on Livestream Curator and sees all online streamers across platforms. 

- A viewer wants to follow a group of streamers. The viewer can group live streamers in a group and quickly see live channels from that group.

- A viewer wants to import a friend's followed streamers list as a starting point for their own list. The viewer logs in and navigates to their friend's profile page, and imports their list.

- A group of streamers wants to create a page showing the live status of their channels and share it with their viewers.

## Requirements
- [ ] Web Pages
	- [ ] User accounts
    	- [x] log in
    	- [x] log out
    	- [x] sign up
    	- [ ] profile page with followed streamers
	- [ ] Manage followed live streamers
    	- [x] Add live streamer
    	- [x] Edit live streamer
    	- [x] Delete live streamer
    	- [x] Create group of live streamers
    	- [x] Edit group 
    	- [x] Delete group
    	- [x] Show group
- [ ] Database Models
	- [x] User
		- username
		- password (hashed)
	- [ ] Livestreamer
		-  user (foreign key)
		-  name
		-  twitchUsername
        -  twitchUserId
		-  youtubeUsername
	- [x] Group
		- user (foreign key)
		- livestreamers (many to many)
		- name
## API Backend
- [x] Authentication

| Endpoint  | Description |
| - | - |
| Auth  | Log in with user and password  |

Auth

POST /auth 

Required request body parameters
| Name  | Type | Description |
| - | - | - |
| username | string | User login name |
| password | string | User password |

Response
| Name  | Type | Description |
| - | - | - |
| token | string | Authentication token |

- [ ] Users

| Endpoint  | Description |
| - | - |
| Get users | Get user info |
| Create user | Create user account |
| Get user's followed live streams  | Retrieve list of live streamers user is following |
| Create livestream followed by user | Add live streamer to a user's followed list |

Get users

Authentication

None

GET /users?username=bob,rachel

Optional request url parameters
| Name  | Type | Description |
| - | - | - |
| username | string | account's username |

Response

| Name | Type | Description |
| - | - | - |
| id | int | User id |
| username | string | account's username |

Create user

Authentication

None

POST /users

Required request body parameters
| Name  | Type | Description |
| - | - | - |
| username | string | account's username |
| password | string | account's password |

Response

| Name | Type | Description |
| - | - | - |
| id | int | User id |
| username | string | User's username |



Get user's followed live streams

Authentication 

None

GET /users/\<user_id>/livestreams

Response 
| Name  | Type | Description |
| - | - | - |
| id | int | livestreamer id |
| name | string | livestreamer's name |
| twitchUsername | string | livestreamer's Twitch username |

Create live streamer followed by user

Authentication

Required scope: user_follows_edit

POST /users/\<user_id>/livestreams

Required request body parameters
| Name  | Type | Description |
| - | - | - |
| name | string | name of live streamer |
| twitchUsername | string | live streamer's Twitch username |

- [ ] Livestreams

| Endpoint  | Description |
| - | - |
| Get live stream | Get live streamer info |
| Update live stream | Update live streamer info |
| Patch live stream | Patch live streamer info |
| Delete live stream | Delete live streamer |


Get live stream

Authentication

Required scope: user_follows_edit,livestream_edit

GET /livestreams/\<livestream_id>

Response
| Name  | Type | Description |
| - | - | - |
| id | int | livestreamer id |
| name | string | livestreamer's name |
| twitchUsername | string | livestreamer's Twitch username |

Update live stream  

Authentication

Required scope: user_follows_edit, livestream_edit

PUT /livestreams/\<livestream_id>

Required request body parameters
| Name  | Type | Description |
| - | - | - |
| name | string | Name of live streamer |

Optional request body parameters
| Name  | Type | Description |
| - | - | - |
| twitchUsername | string | Username of live streamer's Twitch channel |

Response
| Name  | Type | Description |
| - | - | - |
| id | int | livestreamer id |
| name | string | livestreamer's name |
| twitchUsername | string | livestreamer's Twitch username |

Patch (partially update) live stream  

Authentication

Required scope: user_follows_edit, livestream_edit

PATCH /livestreams/\<livestream_id>

Optional request body parameters
| Name  | Type | Description |
| - | - | - |
| name | string | Name of live streamer |
| twitchUsername | string | Username of live streamer's Twitch channel |

Response
| Name  | Type | Description |
| - | - | - |
| id | int | livestreamer id |
| name | string | livestreamer's name |
| twitchUsername | string | livestreamer's Twitch username |

Delete live stream  

Authentication

Required scope: user_follows_edit, livestream_edit

DELETE /livestreams/\<livestream_id>
