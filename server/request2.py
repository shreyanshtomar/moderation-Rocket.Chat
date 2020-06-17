import requests
import base64

payload = {
    "imageUrls" : [
        "https://static.independent.co.uk/s3fs-public/thumbnails/image/2015/06/06/15/Chris-Pratt.jpg?w968h681",
        "https://www.curvyerotic.com/wp-content/uploads/2018/09/nora-rose-scarf-nude-muse-1.jpg",

    ]
}
resp = requests.post("http://localhost:5000/predict",data= payload)

print(resp.json())