pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
        stage('Run') {
            steps {
                sh 'echo "Running Multiiping file"'
                sh '''
                    python multiiping.py
                '''
            }
}
    }
}
