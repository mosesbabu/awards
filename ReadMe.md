# Awards

This python/django web-app was created as a clone of the website 'Awwwards'.
By: Moses Babu

## Description
This web-app allows a user to create a Profile,Category,Country,Technology,Color and Projects that are all under his username allowing other users to vote for them and visit the particular projects site.

## Setup/Installation Requirements
* Live site can be accessed from the following link https://awwwards-clone.herokuapp.com/


### Known Bugs
* Elements re-arrange themselves unequally on different screen sizes.
* Cards disarrange themselves when they're not four in a row.
* Submit button moves to the side when a user with a long username logs in.

### Behaviour Driven Development
* The program should return all projects on the directories page<br>
Given:All projects<br>
When: Url is changed to directory page<br>
Then: All projects are displayed<br>

* Program should show the project with the highest number of votes on the caraousel on the home page<br>
Given:A Project with the highest votes<br>
When: Home page is accessed <br>
Then: Project with highest votes is displayed.<br>

* Admin site should be displayed when "admin/" url is chosen<br>
Given: An admin url<br>
When: User enters admin url in browser<br>
Then: Admin Login is displayed<br>

* User authentication occurs when Admin tries to Login<br>
Given:Admin page is accessed<br>
When: User tries to login<br>
Then: User details are authenticated to confirm if user is an admin<br>

* User session should end when logout url is chosen<br>
Given:Logout option is given<br>
When: User chooses logout option<br>
Then: User session is ended<br>


### Technologies Used
* Git and Github were used as my local and online repositories respectively.
* python Django was used as the framework of choice
* Heroku was used as the host of the live site
* Postman was used in testing the API


### Support and contact details
* Contact me through my email: mosesarara@gmail.com
* The source code is also contained within the folder containing this ReadMe with comments on the code thus third-party support can be offered.

### License
Copyright (c)2020 **Awards by Moses babu**
