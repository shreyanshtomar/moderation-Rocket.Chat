FROM ubuntu:18.04

MAINTAINER shreyansh-tomar
RUN apt-get update && apt-get install -y \
    python3-pip
RUN pip3 install --upgrade pip

RUN pip install torch torchvision

RUN pip install -U Flask
RUN pip install requests

WORKDIR /flaskApp
COPY . /flaskApp

EXPOSE 5000
ENTRYPOINT ["python3" ]
CMD ["server/server.py"]

