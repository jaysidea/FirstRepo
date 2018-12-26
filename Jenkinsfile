pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'docker build -t eero .'
      }}
      stage('Push') {
      steps {
        sh 'docker images'
      }
    }
  }
}
