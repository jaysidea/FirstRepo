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
        sh 'docker login -u spanidea123/eero -p spanidea'
        sh 'docker push spanidea123/eero:PingFile'
      }
    }
  }
}
