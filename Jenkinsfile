pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
				pip install --upgrade pip 
				pip install --upgrade setuptools
                pip install -r requirements.txt
            }
        }
        stage('Test') {
            steps {
                pytest --pylint --cov
            }
        }
    }
}
