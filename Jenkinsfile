pipeline {
        agent any
            stages {
                stage('Clone Repository') {
                /* Cloning the repository to our workspace */
                steps {
                checkout scm
                }
           }
            stage('Initialize'){
        def dockerHome = tool 'mydocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
            }
           stage('Build Image') {
                steps {
                sh 'docker build -t moleculevis .'
                }
           }
           stage('Run Image') {
                steps {
                sh 'docker run -d -p 8501:8501 --name moleculevis moleculevis:v1'
                }
           }
           stage('Testing'){
                steps {
                    echo 'Process Complete..'

                    }
           }
    }
}