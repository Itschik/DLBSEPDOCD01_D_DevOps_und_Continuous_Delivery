pipeline {
    agent any
    environment {
        // Optional: Name für virtuelle Umgebung
        VENV_DIR = "venv"
    }
    
        stages {
            stage('Checkout') {
            steps {
                // Repository aus GitHub klonen
                echo 'Klone Repository...'
                git branch: 'main', url: 'https://github.com/Itschik/DLBSEPDOCD01_D_DevOps_und_Continuous_Delivery.git'
            }
        }

            stage('Setup Python Environment') {
            steps {
                echo 'Erstelle virtuelle Umgebung und installiere Abhängigkeiten...'
                bat """
                    python3 -m venv $VENV_DIR
                    ./$VENV_DIR/bin/pip install --upgrade pip
                    ./$VENV_DIR/bin/pip install -r requirements.txt
                """
            }
        }

            stage('Run Python Script') {
            steps {
                echo 'Starte meine Python-Datei...'
                bat "./$VENV_DIR/bin/cart/tests/test_models.py"
            }
        }
  
        
        stage('Build') {
            steps {
                //
                echo 'Building the application.....'
            }
        }
        stage('Test') {
            steps {
                //
                echo 'Testing the application.....'
            }
        }
        stage('Deploy') {
            steps {
                //
                echo 'Deploying the application.....'
            }
        }

            post {
        success {
            echo 'Pipeline erfolgreich abgeschlossen!'
        }
        failure {
            echo 'Pipeline fehlgeschlagen!'
            }
        }
    }
}
