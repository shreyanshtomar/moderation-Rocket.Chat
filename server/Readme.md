### Run the server
$ FLASK_ENV=development FLASK_APP=server/server.py flask run

### We can use the requests library to send a POST request to our app:
1. Update the path of image you want to test in Request Script
2. Run it!
3. Now check resp.json()
4. check resp.json() output. 
5. Output -> {'class_name': 'sfw'}

### Dependencies
1. Anaconda ("https://docs.anaconda.com/anaconda/install/")
2. PyTorch ("https://pytorch.org/")
3. pip & pip3 ("https://pip.pypa.io/en/stable/installing/")
4. pip install requests && pip3 install requests
5. pip install Flask