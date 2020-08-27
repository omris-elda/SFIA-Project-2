pipeline {
    agent any
    stages {
        stage("Build") {
            steps {
                sh "bash ./scripts/build.sh"
                // build the containers here with docker-compose build perhaps?
                // then send them off to the registry (dockerhub)
            }
        }
        
        stage("Test") {
            steps {
                sh "bash ./scripts/test.sh"
                // test all of the services with
                // pytest --cov application --cov-report term-missing
            }
        }

        stage("Deploy") {
            steps {
                sh "pwd"
                sh "ls"
                sh "docker-compose build -d"
                // deploy to Docker Swarm using the build that was pushed to dockerhub most recently
                // hopefully using docker stack? We'll see.
            }
        }
    }
}
