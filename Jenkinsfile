pipeline {
  agent {
    docker {
      image 'python'
      
    }

  }
  stages {
    stage('1st Stage'){
      steps{
     echo 'Docker/container is ready'
      }
    }
    stage('Get Dependencies') {
      steps {
        sh 'python hello.py'
        sh 'sudo pip install multiping'
      }
    }
    
    stage('Run') {
      steps {
        echo 'Yeah done!!'
        sh 'python multiing.py'
      }
    }
  }
}
