#!/bin/bash

build_image () {
    docker build --rm -f  "sharpbot.Dockerfile" -t sharpbot-facebook:latest .
}

cd ..
git pull
git config core.fileMode false
docker system prune -f

GITLOG=$(git show HEAD --name-only)
FILE="sharpbot.Dockerfile"
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

docker-compose down
docker-compose up -d
