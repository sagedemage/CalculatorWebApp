pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
				sh 'pip install --upgrade pip'
				sh 'pip install --upgrade setuptools'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
				sh 'pytest --pylint --cov'
            }
        }
    }
}
