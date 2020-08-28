#! /bin/bash

pwd
whoami
ls
/home/jenkins/.local/bin/ansible --version
/home/jenkins/.local/bin/ansible-playbook -i inventory.cfg playbook.yaml
docker --version
docker-compose --version
# Delete any previous images
sudo docker images

sudo docker-compose build
sudo docker images
sudo docker system prune -f
# First we have to tag the images with the username of the registry we want to push them to
sudo docker images
sudo docker login
# Then we can actually push them to the registry (Dockerhub)
sudo docker-compose push
