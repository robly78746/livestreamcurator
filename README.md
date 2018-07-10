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