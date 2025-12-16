pipeline {
    agent { label 'Ankita' }

    parameters {
        choice(
            name: 'ENV',
            choices: ['dev', 'qa', 'prod'],
            description: 'Select environment'
        )
    }

    stages {

        stage('Code') {
            steps {
                echo 'Cloning the code'
                git url: 'https://github.com/DevOpswithAnkita/python-app.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image'
                sh 'whoami'
                sh 'docker build -t python-app:${ENV} .'
            }
        }

        stage('Test') {
            steps {
                echo 'Test stage'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def portMap = [
                        dev : '8001',
                        qa  : '8002',
                        prod: '8000'
                    ]

                    sh """
                    docker rm -f python-app-${ENV} || true
                    docker run -d \
                      -p ${portMap[ENV]}:8000 \
                      --name python-app-${ENV} \
                      python-app:${ENV}
                    """
                }
            }
        }
    }
}
