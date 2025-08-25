pipeline {
    agent any
        stages {
            stage('Checkout') {
            steps {
                // Repository aus GitHub klonen
                git branch: 'main', url: 'https://github.com/Itschik/DLBSEPDOCD01_D_DevOps_und_Continuous_Delivery.git'
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
    }
}
