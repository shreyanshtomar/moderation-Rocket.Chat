import torch
import torch.functional as F
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torchvision import datasets, models, transforms

import copy    
import glob
import io
from io import open
import json
import numpy as np
import os, os.path, random
from pathlib import Path
import requests
import time

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
    my_transforms = transforms.Compose([transforms.RandomResizedCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.5, 0.5, 0.5],
                                            [0.5, 0.5, 0.5])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes).to(device)
    outputs = net.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = y_hat.item()
    return class_index[predicted_idx]

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # we will get the file from the request
        file = request.files['file']
        # convert that to bytes
        img_bytes = file.read()
        class_name = get_prediction(image_bytes=img_bytes)
        return jsonify({'class_name': class_name})


if __name__ == '__main__':
    app.run()