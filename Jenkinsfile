pipeline {
    agent any
    stages {
        stage("Build") {
            steps {
                sh "pwd"
                sh "whoami"
                sh "ls"
                // build the containers here with docker-compose build perhaps?
                // then send them off to the registry (dockerhub)
            }
        }
        
        stage("Test") {
            steps {
                sh "pwd"
                sh "ls"
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
