pipeline {
  agent {
    docker {
      image 'python'
      args '-u root:root'
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
        sh 'python -m pip install multiping'
        
      }
    }
    
    stage('Run') {
      steps {
        echo 'Yeah done!!'
        
      }
    }
  }
}
