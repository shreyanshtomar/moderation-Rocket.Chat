import requests

payload = {
      'image_url': [
            "https://unsplash.com/photos/I2fStgjOyAg/download?force=true",
            "https://unsplash.com/photos/-Hm_xIcYbUY/download?force=true&w=640"
      ]
}

resp = requests.post("http://localhost:5000/predict", json = payload)

print(resp.json())