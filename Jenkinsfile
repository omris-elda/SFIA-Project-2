pipeline {
    agent any
    stages {
        stage("Build") {
            steps {
                sh "pwd"
                sh "whoami"
                sh "ls"
                sh "ansible -v"
                sh "ansible-playbook -i inventory.cfg playbook.yaml"
                // build the containers here with docker-compose build perhaps?
                // then send them off to the registry (dockerhub)
            }
        }
        
        stage("Test") {
            steps {
                sh "pwd"
                sh "ls"
                sh "cd app1"
                sh "pytest --cov application --cov-report term-missing"
                sh "cd .."
                sh "cd app2"
                sh "pytest --cov application --cov-report term-missing"
                sh "cd .."
                sh "cd app3"
                sh "pytest --cov application --cov-report term-missing"
                sh "cd .."
                sh "cd app4"
                sh "pytest --cov application --cov-report term-missing"
                sh "cd .."
                // test all of the services with
                // pytest --cov application --cov-report term-missing
            }
        }

        stage("Deploy") {
            steps {
                sh "pwd"
                sh "ls"
                // deploy to Docker Swarm using the build that was pushed to dockerhub most recently
                // hopefully using docker stack? We'll see.
            }
        }
    }
}
