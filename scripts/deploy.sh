#! /bin/bash

pwd
ls
ssh swarm-manager
git clone https://github.com/omris-elda/SFIA-Project-2.git
cd SFIA-Project-2
sudo docker stack deploy --compose-file docker-compose.yaml
sudo docker images
sudo docker container ls