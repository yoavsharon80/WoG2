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
                   sh 'sleep 40'
            }
        }
        stage ('dir change'){
            steps{
                sh 'cd tests'
            }
        }
        stage('run e2e test'){
            steps {
                sh 'python3 tests//e2e.py'
                sh 'sleep 30'
            }
        }
        stage('Docker tear down') {
            steps {
                sh 'docker-compose down'
                sh 'docker rmi wog2_web'
            }
        }
    }
}
