pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps {
                git 'https://github.com/yoavsharon80/day8.git' 
            }
        }
        stage('Docker Bring up') {
            steps {
                sh 'docker-compose up'
            }
        }
        stage('run e2e test'){
            steps {
                sh 'cd tests'
                sh 'python3 e2e.py'
            }
        }
    }
}
