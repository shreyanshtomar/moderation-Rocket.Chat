# Content Moderation

Due to interactions between large communities among different channels in Rocket Chat, there was a need for support of an optional moderation service for offensive content. The service as of now is limited to image & links moderation which means if someone sends an offensive image or link to Rocket Chat app and the app along with server is deployed and configured then the image will be blocked but not videos.
The dockerised moderation service can be deployed to any server easily since all the major Cloud Providers such as AWS, GCP, Azure, IBM Cloud, etc. provides support to Docker.

![ezgif com-optimize](https://user-images.githubusercontent.com/18248623/89886718-babcff80-dbea-11ea-9c19-afee96f9aff1.gif)


## Quick start for code developers
Prerequisites:

* [RC-Deploy](https://docs.rocket.chat/apps-development/getting-started#installation)
* [Docker](https://docs.docker.com/get-docker/)
> Depending on the installation & machine while running docker commands you may want to use 'sudo' if you encounter any errors.

```sh
1. git clone https://github.com/shreyanshtomar/moderation
2. cd moderation
3. docker-compose up -d
```
4. Open RC instance ( http://127.0.0.1:3000 ).
5. Generate Personal Access Tokens(`My Account -> Personal Access Tokens -> Add `)
Copy User-ID & Token for future use.
6. From Rocket Chat open Administration -> General -> Apps -> Enable App development mode & Enable the App Framework.<br>
Switch to Command Line(terminal).
```sh
7. cd content-moderation
8. npm install # You may want to use sudo if you encounter any errors in next step!
9. rc-apps deploy --url http://127.0.0.1:3000 --username <your-user-name> --password <your-password>

After the first time deployment of app if you change anything in App's code than add an '--update' flag at the end in the above command.
```
> After deployment let's configure Content Moderation App so that app can help in posting images to the hosted moderation-service to make predictions and
block offensive images/links.<br>
In our case:<br>
10. Administration -> Apps -> Content Moderation.<br>
'Rocket Chat host URL': http://rocket-chat:3000 &  'Content Moderation App Host URL': http://moderation-api:5000/predict in
Content Moderation App's Setting.<br>
Now, Let's deploy our service!!<br>
11. Edit [docker-compose-server.yml](https://github.com/shreyanshtomar/moderation/blob/shreyansh_dev/docker-compose-server.yml) in your local moderation folder
(directory) & change the following
parameters:<br>
  a. [RC_UUID](https://github.com/shreyanshtomar/moderation/blob/38da4fc779bbaa74e54153aaa0ba0f537e55f563/docker-compose-server.yml#L13) <br>
  b. [RC_TOKEN](https://github.com/shreyanshtomar/moderation/blob/38da4fc779bbaa74e54153aaa0ba0f537e55f563/docker-compose-server.yml#L14)<br>
  We copied them in 5th Step.
```sh
 12. cd .. # Make sure you're in moderation directory
 13. docker-compose -f docker-compose-server.yml up -d
 ```
 ## Everything is configured now. We can now test the app!!.
 Try posting an offensive image in one of the channels & it should get blocked!
 
 To see the **logs** generated:
 ```sh
 docker logs moderation_rocketchat_1
 docker logs moderation_api_1
 ```
 

