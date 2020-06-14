import requests

path = 'tests/test_images/park.jpeg'
resp = requests.post("http://localhost:5000/predict",files={"file": open(path,'rb')})

print(resp.json()) #Response recieved from the end point.