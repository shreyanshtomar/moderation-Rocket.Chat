import requests
import base64

payload = {
      'imageUrls': [
            "https://unsplash.com/photos/I2fStgjOyAg/download?force=true",
            "https://www.photo-kako.com/sample/low-image-quality.jpg"
      ]
}

resp = requests.post("http://localhost:5000/predict", json = payload)

print(resp.json())