pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'docker build -t localhost:5000/local-eero:newpingfile .'
      }}
      stage('Push') {
      steps {
        sh 'docker push localhost:5000/local-eero:newpingfile'
        sh 'docker pull localhost:5000/local-eero:newpingfile'
      }
    }
    stage('Pull') {
      steps {
        echo "Login"
        
      }
    }
  }
}
