#! /bin/bash

pwd
ls
ssh swarm-manager
ls
pwd
whoami
# make sure there's no residual images
sudo docker images
sudo docker rmi ormiselda/app1:latest
sudo docker rmi ormiselda/app2:latest
sudo docker rmi ormiselda/app3:latest
sudo docker rmi ormiselda/app4:latest
sudo docker rmi ormiselda/app1
sudo docker rmi ormiselda/app2
sudo docker rmi ormiselda/app3
sudo docker rmi ormiselda/app4
sudo docker images
# Clone the repo down so that I can use the docker-compose.yaml
git clone https://github.com/omris-elda/SFIA-Project-2.git
ls
cd SFIA-Project-2
sudo docker stack deploy --compose-file docker-compose.yaml project2
sudo docker images
sudo docker container ls
rm -r SFIA-Project-2
ls
