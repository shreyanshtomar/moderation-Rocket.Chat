### Run the server
Run the server.py script to start the server which serves as one endpoint.

$ FLASK_ENV=development FLASK_APP=server/server.py flask run

### We can use the requests library in python to send a POST request to our app:
1. Update the path of image you want to test in Request Script(request.py).
2. Run the request.py script and check the output for prediction. ("$ python3 server/request.py").
3. Output -> {'class_name': 'sfw'} (depends of type of image in this case the image is of the park(sfw)).

### Dependencies
1. Anaconda ("https://docs.anaconda.com/anaconda/install/")
2. PyTorch ("https://pytorch.org/")
3. pip & pip3 ("https://pip.pypa.io/en/stable/installing/")
4. pip install requests && pip3 install requests
5. pip install Flask