pipeline{
    agent any

    environment {
        VIRTUAL_ENVIRONMENT = "${WORKSPACE}/venv"
    }

    stages {
        stage ('Checkout Code'){
            steps{
                git url: 'https://github.com/Nandeesh-24/Automation_Practice1'
            }
        }

        stage('Setup python environment'){
            steps{
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run tests'){
            steps{
                sh './venv/bin/pytest --alluredir=allure-results'
            }
        }

        stage('Allure report'){
            steps{
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }
    }

    post{
        always{
            archiveArtifacts artifacts: 'allure-results/**/*', allowEmptyArchive: true
            junit 'tests/reports/*.xml'
        }
    }
}