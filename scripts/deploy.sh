#!/bin/bash

# chmod u+x deploy.sh
# For new install

build_image () {
    $SUDO docker build --rm -f "Dockerfile" -t sharpbot-discord:latest .
}

NAMEOUT="$(uname)"
if [[ $NAMEOUT =~ "MINGW" ]]; then
    SUDO=""
else
    SUDO="sudo"
fi

git pull
git config core.fileMode false
$SUDO docker system prune -f
mkdir -p sharpbot/data

docker_version="$($SUDO docker version)"
RESULT=$?
if [[ $RESULT != 0 ]]; then
    echo "docker must be installed for deployment. Exiting..."
    exit
else
    echo "Found docker"
fi

docker_version="$($SUDO docker-compose version)"
RESULT=$?
if [[ $RESULT != 0 ]]; then
    echo "docker-compose must be installed for deployment. Exiting..."
else
    echo "Found docker-compose"
fi


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

$SUDO docker-compose down
$SUDO docker-compose up -d
$SUDO docker-compose logs -f
