#!/bin/bash

# sudo chmod u+x deployunix.sh
# For new install

build_image () {
    sudo docker build --rm -t sharpbot-facebook:latest .
}

cd ..
sudo git pull
sudo git config core.fileMode false
sudo docker system prune -f
sudo mkdir -p sharpbot/data

GITLOG=$(git show HEAD --name-only)
FILE="Dockerfile"
if [[ $GITLOG =~ $FILE ]];
then
    build_image
else
    echo "No changes to dockerfile"
fi

FILE=.env
if [[ ! -f $FILE ]]; then
    touch .env
    read -p "Please enter your email: " -r
    LINE="EMAIL=$REPLY"
    read -p "Please enter your password: " -r
    echo "PASS=$REPLY
$LINE
MODS=[]
ADMINS=[]"> .env
else
    echo ".env exsists..."
fi

sudo docker-compose down
sudo docker-compose up -d
