pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'docker build -t localhost:5000/local-eero:newpingfile .'
      }}
      stage('Push') {
      steps {
        sh 'docker images localhost:5000/local-eero'
        sh 'docker pull localhost:5000/local-eero'
      }
    }
    stage('Pull') {
      steps {
        echo "Login"
        
      }
    }
  }
}
