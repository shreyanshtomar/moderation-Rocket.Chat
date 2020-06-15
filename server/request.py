import requests
import base64

path = 'tests/test_images/people.jpeg'
image_file_handle = open(path, "rb")
base64_string = base64.b64encode(image_file_handle.read())
resp = requests.post("http://localhost:5000/predict",files={"file": base64_string})

print(resp.json())