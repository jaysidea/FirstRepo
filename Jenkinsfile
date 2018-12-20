pipeline {
  agent {
    docker {
      image 'python'
      
    }

  }
  stages {
    stage('Get Dependencies') {
      steps {
        sh 'pip install multiping'
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
