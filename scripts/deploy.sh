#! /bin/bash

pwd
ls
ssh swarm-manager << EOF
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
sudo docker pull omriselda/app1:latest
sudo docker pull omriselda/app2:latest
sudo docker pull omriselda/app3:latest
sudo docker pull omriselda/app4:latest
sudo docker pull omriselda/nginx:latest

sudo docker images
sudo docker tag omriselda/app1 app1
sudo docker tag omriselda/app2 app2
sudo docker tag omriselda/app3 app3
sudo docker tag omriselda/app4 app4
sudo docker tag omriselda/nginx nginx

sudo docker images
sudo docker stack deploy --compose-file docker-compose.yaml project2
sudo docker images
sudo docker container ls -a
sudo docker stack services project2
cd ..
rm -r SFIA-Project-2
# sudo docker service scale project2_service1=10
# sudo docker service scale project2_service2=10
# sudo docker service scale project2_service3=10
# sudo docker service scale project2_service4=10
# sudo docker service scale project2_nginx=10
sudo docker stack services project2
ls

EOF