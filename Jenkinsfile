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
        sh 'docker run -d -p 5000:5000 --restart=always --name registry registry:2'
        sh 'docker tag eero localhost:5000/local-eero'
        
      }
    }
  }
}
