# our base image
FROM python:3.10.5-alpine

# set working directory inside the image
WORKDIR /app

# copy our requirements
COPY requirements.txt requirements.txt

# install dependencies
RUN pip3 install -r requirements.txt

# copy this folder contents to image
COPY . .

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
