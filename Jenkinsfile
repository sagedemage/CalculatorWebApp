pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
				sh 'pip install --upgrade pip'
				sh 'pip install --upgrade setuptools'
                sh 'pip install -r requirements.txt'
				sh 'pip install pytest'
				sh 'pip install pytest-pylint'
				sh 'pip install pytest-cov'
            }
        }
        stage('Test') {
            steps {
				sh 'pytest --pylint --cov'
            }
        }
    }
}
