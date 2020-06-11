import requests

path = 'test_images/park.jpeg'
resp = requests.post("http://localhost:5000/predict",files={"file": open(path,'rb')})