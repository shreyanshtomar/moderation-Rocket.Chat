### Run the server
$ FLASK_ENV=development FLASK_APP=server/server.py flask run

### We can use the requests library to send a POST request to our app:
1. Update the path of image in Request Script
2. Run it!
# Now check resp.json()
# >>> resp.json()
# {'class_name': 'sfw'} //Output