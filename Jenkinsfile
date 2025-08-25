pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Klone Repository...'
                git branch: 'main', url: 'https://github.com/Itschik/DLBSEPDOCD01_D_DevOps_und_Continuous_Delivery.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Erstelle virtuelle Umgebung und installiere Abhängigkeiten...'
                bat """
                    '${tool 'Python3.13'}\\python.exe -m venv %VENV_DIR%'
                    %VENV_DIR%\\Scripts\\pip install --upgrade pip
                    %VENV_DIR%\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Run Python Script') {
            steps {
                echo 'Starte meine Python-Datei...'
                bat "%VENV_DIR%\\Scripts\\python cart\\tests\\test_models.py"
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application.....'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing the application.....'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application.....'
            }
        }
    } // Ende stages

    post {
        success {
            echo 'Pipeline erfolgreich abgeschlossen!'
        }
        failure {
            echo 'Pipeline fehlgeschlagen!'
        }
    }
}
