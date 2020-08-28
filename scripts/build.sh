#! /bin/bash

pwd
whoami
ls
/home/jenkins/.local/bin/ansible --version
/home/jenkins/.local/bin/ansible-playbook -i inventory.cfg playbook.yaml
docker --version
docker-compose --version
sudo docker-compose build
sudo docker images
# First we have to tag the images with the username of the registry we want to push them to
sudo docker tag app1 omriselda/app1:latest
sudo docker tag app2 omriselda/app2:latest
sudo docker tag app3 omriselda/app3:latest
sudo docker tag app4 omriselda/app4:latest
# Then we can actually push them to the registry (Dockerhub)
sudo docker push omriselda/app1:latest
sudo docker push omriselda/app2:latest
sudo docker push omriselda/app3:latest
sudo docker push omriselda/app4:latest
