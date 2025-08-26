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
                    "${tool 'Python3.13'}\\python.exe" -m venv %VENV_DIR%
                    %VENV_DIR%\\Scripts\\python.exe -m pip install --upgrade pip
                    %VENV_DIR%\\Scripts\\pip install -r requirements.txt
                """
            }
        }


        stage('Run Tests') {
            steps {
                echo 'Starte Django-Tests...'
                bat """
                    %VENV_DIR%\\Scripts\\python manage.py test
                """
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
