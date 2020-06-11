import requests

path = '/Users/shrenitomar/Documents/shreyansh/github/moderation/server/park.jpeg'
resp = requests.post("http://localhost:5000/predict",files={"file": open(path,'rb')})

#Now check resp.json()
# >>> resp.json()
# {'class_name': 'sfw'} //Output