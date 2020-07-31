# Content Moderation

Due to interactions between large communities among different channels in Rocket Chat, there was a need for support of an optional moderation service for offensive content. The service as of now is limited to image moderation which means if someone sends an offensive image to Rocket Chat app and the app along with server is deployed and configured then the image will be blocked but not videos.
The dockerised moderation service can be deployed to any server easily since all the major Cloud Providers such as AWS, GCP, Azure, IBM Cloud, etc. provides support to Docker.

## Quick start for code developers
Prerequisites:

* [Git](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Meteor](https://www.meteor.com/install)

> Meteor automatically installs a hidden [NodeJS v12](https://nodejs.org/download/release/v12.16.1/) and [MongoDB v4.2](https://docs.mongodb.com/manual/introduction/) to be used when you run your app in development mode using the `meteor` command.

Now just clone and start the app:

```sh
git clone https://github.com/RocketChat/Rocket.Chat.git
cd Rocket.Chat
meteor npm install
meteor npm start
```
Open http://localhost:3000 or http://127.0.0.1:3000 to start the RC and set it up with your username and password!

## To either simply test the Content-Moderation-App on your local RC instance or contribute to development.

```sh
git clone https://github.com/shreyanshtomar/moderation
cd moderation
docker-compose build
docker-compose up // The server to which RC sends the images and text for moderation purposes.
cd content-moderation
rc-apps deploy --url http://127.0.0.1:3000 --username <your-user-name> --password <your-password>

After the first time deployment of app if you change anything in code than add an '--update' flag at the end in the above command.
```
Provide 'Rocket Chat host URL': http://127.0.0.1:3000 &  'Content_Moderation_App Host URL': http://127.0.0.1:5000/predict in 
Content Moderation App's Setting section in RC instance which can be found by following the steps mentioned below:
1. In options section open administration.
2. Go to apps.
3. Look out for Content Moderation App & enable it.
