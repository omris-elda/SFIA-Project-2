#! /bin/bash
pwd
ls
pip3 install -r requirements.txt

cd app1
python3 -m pytest --cov app --cov-report term-missing
cd ..

cd app2
python3 -m pytest --cov app --cov-report term-missing
cd ..

cd app3
python3 -m pytest --cov app --cov-report term-missing
cd ..

cd app4
python3 -m pytest --cov app --cov-report term-missing
cd ..