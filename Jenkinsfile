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
        sh 'docker tag pingfile localhost:5000/local-eero'
        sh 'docker push localhost:5000/local-eero'
        
      }
    }
  }
}
