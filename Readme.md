# moderation
This repo contains all the files related to Rocket.Chat app development for Content Moderation

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
There are two methods to do it.
```sh
cd moderation
docker build -t serverapp:latest .
docker run -t -d -p 5000:5000 --network=host serverapp // The server to which RC sends the images and text for moderation purposes.
cd content-moderation
rc-apps deploy --url http://127.0.0.1:3000 --username <your-user-name> --password <your-password>

After the first time deployment of app if you change anything in code than add an '--update' flag at the end in the above command.
```
Provide 'Rocket Chat host URL': http://127.0.0.1:3000 &  'Content_Moderation_App Host URL': http://127.0.0.1:5000/predict in 
Content Moderation App's Setting section in RC instance.