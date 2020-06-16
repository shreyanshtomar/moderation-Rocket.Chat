import torch
import torch.functional as F
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torchvision import datasets, models, transforms
from service_streamer import ThreadedStreamer

import copy    
import glob
import io
from io import open
import json
import os, os.path, random
from pathlib import Path
import time

import re
import base64
from PIL import Image
from flask import Flask, jsonify, request

app = Flask(__name__)

#Automatically detects if the device is CUDA enabled to run GPU inferences.
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
device_avail = torch.cuda.is_available()

class_index = {0: 'nsfw', 1: 'sfw'}
net = models.resnet18(pretrained=True)
net = net.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.0001, momentum=0.9)

num_ftrs = net.fc.in_features
net.fc = nn.Linear(num_ftrs, 128)
net.fc = net.fc.to(device)

path = Path('server/resnet18_checkpoint.pth') #Path to the checkpoint(weight)

#Preparing model for evaluation based on device's capability
if not device_avail:
    net.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
else:
    net.load_state_dict(torch.load(path))
net.eval()

#Preprocess Image
def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(base64.decodebytes(image_bytes)))
    return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes).to(device)
    outputs = net.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = y_hat.item()
    return class_index[predicted_idx]

def batch_prediction(image_bytes_batch):
    image_tensors = [transform_image(image_bytes=image_bytes) for image_bytes in image_bytes_batch]
    tensor = torch.cat(image_tensors).to(device)
    outputs = net.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_ids = y_hat.tolist()
    return [class_index[i] for i in predicted_ids]

streamer = ThreadedStreamer(batch_prediction, batch_size=64)

@app.route('/', methods=['GET'])
def root():
    return jsonify({'msg' : 'Try POSTing to the /predict endpoint with an RGB image attachment'})

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # we will get the file from the request
        file = request.files['image']
        #image_data = re.sub('^data:image/.+;base64,', '', request.form['data'])
        # convert that to bytes
        img_bytes = file.read()
        class_name = streamer.predict([img_bytes])[0]
        if(class_name == 'nsfw'):
            return jsonify({0 : class_name})

        elif(class_name == 'sfw'):
            return jsonify({1 : class_name})

        return jsonify({'class_name': class_name})


if __name__ == '__main__':
    app.run(debug=True)
    