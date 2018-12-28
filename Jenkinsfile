pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'docker build -t spanidea123/eero:PingFile .'
      }}
      stage('Push') {
      steps {
        sh 'docker images'
        sh 'docker image tag pingFile localhost:5000/eeroImages'
        sh 'docker push localhost:5000/eeroImages'
      }
    }
  }
}
