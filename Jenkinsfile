pipeline {
    agent any
    stages{
        stage('checkout code'){
            steps{
                git url:'https://github.com/Rahul-P-2023/jenkdocgit.git',branch:'main'

            }
        }
        stage('build image'){
            steps{
                bat 'docker build -t myimage'
            }
        }
        stage('create container'){
            steps{
                bat 'docker run -d -p 8501:8501 myimage'
            }
        }
    }

}