Your tree should look (more or less) like this:
```
├── Dockerfile
├── app.py
├── requirements.txt
├── static
│   ├── maybe you have things here
│   │   └── stuff
│   └── maybe you don't
│       └── more things
└── templates
    ├── index.html
    ├── other.html
    .
    .
    .
```
Assuming you just need `python`, the Dockerfile should be:

```
FROM python

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "app.py" ] 
```

At a minimum, requirements.txt should have `flask` in it. Add anything else that your app requires (beyond base python packages) as a new line.

In a terminal, cd into the parent directory. We need to build a docker image from the contents of this directory.

```
docker image build -t <your_app_name>:<your_version_number> .
```

The `-t` tags the image with a name and version. The `.` specifies bulding the image from everything in the current working directory of the terminal.  


Now let's test it locally.

```
docker container run -p 8080:8080 -d --name <your_container_name> <your_app_name>:<your_version_number>
```

`-p` connects the port that the Dockerfile exposed to the machine's port. `--name` names the container.

Go to localhost:8080 and check your work.

Everything should be up and running.

Now we want to push this up to your dockerHub.

Make sure you're logged in to docker account.

```
docker image ls
```

and copy the `IMAGE_ID`. To do the actual push:
```
docker tag <the_image_id> <your_dockerHub_name>/<your_app_name>:<your_version_number>

docker push <your_dockerHub_name>/<your_app_name>
```

Things should happen.

Neat.

If you have an EC2 you want to use that already had docker on it, great. Use that instance.

Otherwise, go spin up an amazon linux based EC2. The os here makes installing docker quite easy. SSH into that puppy and:

```
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
```

end and restart the ssh connection to have the `usermod` take effect.

Assuming you kept your dockerHub repo public, you can simply:

```
docker pull <your_dockerHub_name>/<your_app_name>:<your_version_number>
```

Assuming you want to be able to just go to the EC2's web address and see your site, open port 80 on EC2's security group's inbound and outbound rules. While you're there, make sure the EC2's AIM role doesn't have access to... anything. This instance is pretty much wide open to ne'er-do-wells.

on the EC2 run:

```
docker container run -p 80:8080 -d --name <your_app_name> <your_image_id>

docker start <your_app_name>
```

The `-d` here detaches the EC2's terminal from the docker container; you don't need to screen the session on your local machine to have this keep running. Also, the last line of the `Dockerfile` runs `app.py` so the app should be up and running without the need for running `app.py` in an interactive terminal.

Check it out!

I take no credit for this working or not. 

Godspeed,

Hunter