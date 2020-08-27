#! /bin/bash
pwd
ls
cd app1
pytest --cov app --cov-report term-missing
cd ..

cd app2
pytest --cov app --cov-report term-missing
cd ..

cd app3
pytest --cov app --cov-report term-missing
cd ..

cd app4
pytest --cov app --cov-report term-missing
cd ..