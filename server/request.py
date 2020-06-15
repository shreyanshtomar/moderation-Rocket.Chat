import requests

path = 'tests/test_images/people.jpeg'
resp = requests.post("http://localhost:5000/stream_predict",files={"file": open(path,'rb')})

print(resp.json()) #Response recieved from the end point.