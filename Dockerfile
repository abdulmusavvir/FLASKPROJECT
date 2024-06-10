FROM python:3.8-slim-buster
WORKDIR /FLASKPROJECT
COPY requirement.txt requirement.txt
RUN pip install --upgrade pip && pip install -r requirement.txt
EXPOSE 8096
COPY . .
CMD [ "python3","-m","flask","run","--host=0.0.0.0", "--port=8096" ]
