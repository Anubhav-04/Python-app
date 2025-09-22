pipeline {
    agent any
    stages {
        stage('Bulding App') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install pytest
                '''
            }
        }
        stage('Run application') {
            steps {
                sh 'python3 calculate.py'
            }
        }
        stage('Test application') {
            steps {
                sh 'python3 app.test.py'
            }
        }
    }
}