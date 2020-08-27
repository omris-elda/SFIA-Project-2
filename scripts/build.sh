#! /bin/bash

pwd
whoami
ls
ansible --version
ansible-playbook -i inventory.cfg playbook.yaml