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
        sh 'docker login -u spanidea123 -p Jayram@1990'
        sh 'docker push spanidea123/eero:PingFile'
      }
    }
  }
}
