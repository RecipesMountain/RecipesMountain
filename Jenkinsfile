pipeline {
   environment{
        DOCKER_REPO_ADDRESS = "http://localhost:8090/"
        registryCred = "nexus-cred"
        imageName = "backend-test"
        dockerImg = ''
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
          docker-compose up -d
          cd services/backend
          docker build --target=test  -t backend-test .
          docker login -u=admin -p=1234 http://localhost:8090/repository/docker-RecipesMountain-repo/
          docker tag backend-test localhost:8090/testname/backendtest:1
          docker push localhost:8090/testname/backendtest:1
          echo 'Testing Nexus pushing'
          """
//           dockerImg = docker.build("${imageName}", "./services/backend")
          sh 'echo "Testing Nexus pushing"'
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
          docker run -i --env-file .env  --network recipesmountain_jenkinsci_default --link  postgres-recipemountain:database backend-test '/venv/bin/pytest'
          """
        }
      }
    }
    stage('Test coverage') {
      steps {
        script {
          sh """
          export filehash=\$(find services/backend/ -type f -print0  | xargs -0 sha1sum | awk '{print \$1}' | sha1sum | awk '{print \$1}' )
          docker run -i  -v /shared:/shared --env-file services/backend/.env  --network recipesmountain_jenkinsci_default --link  postgres-recipemountain:database backend-test '/bin/sh' '-c' "/venv/bin/coverage run -m pytest && mkdir -p /shared/\$filehash && /venv/bin/coverage html -d /shared/\$filehash" 
          """       
        }
      }
    }
    stage('Publish to repo'){
      steps{
        script {
          sh """
          echo 'Pushing docker image to Nexus repository'
          docker-compose up -d
          cd services/backend
          docker build --target=test  -t backend-test .
          docker login -u=admin -p=1234 http://localhost:8090/repository/docker-RecipesMountain-repo/
          docker tag backend-test localhost:8090/testname/backendtest:2
          docker push localhost:8090/testname/backendtest:2
          """       
        }
      }
    }
  }  
}
