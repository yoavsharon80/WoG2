pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps {
                git 'https://github.com/yoavsharon80/WoG2.git' 
            }
        }
        stage('Docker Bring up') {
            steps {
                sh 'docker-compose up &'
            }
        }
        stage ('dir change'){
            steps{
                sh 'pwd'
            }
        }
        stage('run e2e test'){
            steps {
                sh 'python3 e2e.py'
            }
        }
    }
}
