pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
				pip install --upgrade pip 
				pip install --upgrade setuptools
                pip install -r requirements.txt
				pip install pytest
				pip install pytest-pylint
				pip install pytest-cov
            }
        }
        stage('Test') {
            steps {
				python -m pytest --pylint --cov
            }
        }
    }
}
