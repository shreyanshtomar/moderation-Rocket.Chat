FROM python:3

MAINTAINER shreyansh-tomar

RUN pip install --upgrade pip

RUN pip install torch torchvision

RUN pip install -U Flask
RUN pip install requests

WORKDIR /app
COPY . /app

EXPOSE 5000
ENTRYPOINT ["python" ]
CMD ["server/server.py"]

