# moderation
This repo contains all the files related to Rocket.Chat app development for Content Moderation

## Running the server and Testing it.

### Run the server
Run the server.py script to start the server which serves as one endpoint.

$ FLASK_ENV=development FLASK_APP=server/server.py flask run

### We can use the requests library in python to send a POST request to our server app:(for testing purposes)
On another terminal/cmd Do these..

1. Update the urls of image you want to test in Request Script(request.py).
2. Run the request.py script and check the output for prediction. ("$ python3 server/request.py").
3. Output(response) -> {'class_name': 'sfw'} (depends of type of image).

### Dependencies
1. Anaconda ("https://docs.anaconda.com/anaconda/install/")
2. PyTorch ("https://pytorch.org/")
3. pip ("https://pip.pypa.io/en/stable/installing/")
4. pip install -r requirements.txt
