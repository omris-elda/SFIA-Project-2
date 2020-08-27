#! /bin/bash

pwd
whoami
ls
ansible --version
ansible-playbook -i inventory.cfg playbook.yaml
docker --version
docker-compose --version
docker-compose build -d
