pipeline {
    agent any

    environment {
        TARGET = "ec2-user@TARGET_SERVER_IP"
        APP_DIR = "/opt/food-ordering"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/food-ordering-flask.git'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                    pytest -q
                '''
            }
        }

        stage('Deploy to Target Server') {
            steps {
                sh '''
                    ssh -o StrictHostKeyChecking=no ${TARGET} "sudo mkdir -p ${APP_DIR} && sudo chown -R ec2-user:ec2-user ${APP_DIR}"
                    scp -o StrictHostKeyChecking=no -r app.py requirements.txt templates static ${TARGET}:${APP_DIR}/
                    ssh -o StrictHostKeyChecking=no ${TARGET} "
                        cd ${APP_DIR} &&
                        python3 -m venv venv &&
                        source venv/bin/activate &&
                        pip install -r requirements.txt &&
                        sudo pkill -f 'gunicorn.*app:app' || true &&
                        nohup venv/bin/gunicorn --bind 0.0.0.0:5000 app:app > app.log 2>&1 &
                    "
                '''
            }
        }
    }

    post {
        success {
            echo 'FoodExpress deployed successfully to Target Server!'
        }
        failure {
            echo 'Deployment failed. Check Jenkins console output.'
        }
    }
}
