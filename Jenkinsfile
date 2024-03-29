pipeline {
   environment{
        DOCKER_REPO_ADDRESS = "http://localhost:8090/"
        registryCred = "nexus-cred"
        imageName = "backend-test"
        dockerImg = ''
        partOfMess = "Build: ${env.BUILD_TAG} on branch ${env.BRANCH_NAME}"
    }
  options {
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  }
  agent any
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Checkout') { // Checkout (git clone ...) the projects repository
      steps {
        checkout scm
      }
    }
    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
          sh """
          docker-compose up -d postgres
          cd services/backend
          docker build --target=test  -t backend-test .
          """
        }
      }
    }
    stage('Linting') {
      steps {
        script {
          sh """
          cd services/backend
          docker run -i backend-test '/venv/bin/black' '--check' '--diff' '--verbose'  '.' 
          """
        }
      }
    }
    stage('Unit Testing') { // Perform unit testing
      steps {
        script {
          sh """
          cd services/backend
          docker run -i --env-file ../../postgres.env --env-file ../../backend.env  --network recipesmountain_ps-44-betterci_default --link  postgres-recipemountain:database backend-test '/venv/bin/pytest'
          """
        }
      }
    }
    stage('Test coverage') {
      steps {
        script {
          sh """
          export fileName="${env.BRANCH_NAME}-${BUILD_TIMESTAMP}"
          docker run -i  -v /shared:/shared --env-file postgres.env --env-file backend.env --network recipesmountain_ps-44-betterci_default --link  postgres-recipemountain:database backend-test '/bin/sh' '-c' "/venv/bin/coverage run -m pytest && mkdir -p /shared/\$fileName && /venv/bin/coverage html -d /shared/\$fileName" 
          """       
        }
      }
    }
    stage('Publish to repo'){
       when{
           branch "main"
       }
      steps{
         
        script {
          sh """
          echo 'Pushing docker image to Nexus repository'
          cd services/backend
          docker build -t backend .
          docker login -u=admin -p=1234 http://localhost:8090/repository/docker-RecipesMountain-repo/
          docker tag backend localhost:8090/releases/backend:${env.BUILD_NUMBER}
          docker push localhost:8090/releases/backend:${env.BUILD_NUMBER}
          """       

        }
      }
    }
  }
  post{
      success{
        slackSend channel: 'jenkins-ci-sages-4', color: 'good', message:  partOfMess + " finished with success.  Coverage Raport: http://localhost:8000/${env.BRANCH_NAME}-${BUILD_TIMESTAMP}/"
      }
      
      failure{
        slackSend channel: 'jenkins-ci-sages-4', color: 'danger', message: partOfMess + ' failed.'
      }
  }  
}
