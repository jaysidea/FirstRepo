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
        sh 'sudo python3 -m pip install multiping'
        
      }
    }
    
    stage('Run') {
      steps {
        echo 'Yeah done!!'
        
      }
    }
  }
}
