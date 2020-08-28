#! /bin/bash

pwd
ls
ssh swarm-manager
pwd
whoami
git clone https://github.com/omris-elda/SFIA-Project-2.git
# cd SFIA-Project-2
sudo docker stack deploy --compose-file docker-compose.yaml SFIA-Project-2
sudo docker images
sudo docker container ls
rm -r SFIA-Project-2