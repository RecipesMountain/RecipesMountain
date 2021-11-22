pipeline {
    agent any

    stages {
        stage('Hello world') {
            steps {
                echo 'Hello world'
                //slackSend channel: 'jenkins-ci-sages-4', message: 'Test succeded'
                echo "build URL is ${env.BUILD_URL}"
                echo "build workplace is ${env.WORKSPACE}"
            }
            
        }
    }
}
