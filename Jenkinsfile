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
        echo 'multiping installation completed'
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
