pipeline {
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
          """
        }
      }
    }
    stage('Linting') { // Run pylint against your code
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
    stage('Test coverage') { // Perform unit testing
      steps {
        script {
          sh """
          export filehash=\$(find services/backend/* -type f \\( -exec sha1sum "\$PWD"/{} \\; \\) | awk '{print \$1}' | sort | sha1sum)
          docker run -i --env-file services/backend/.env  --network recipesmountain_default --link  postgres-recipemountain:database backend-test '/venv/bin/coverage' 'run' '-m' 'pytest' 
          docker run -i -v /shared:/shared --env-file .env-test  --network recipesmountain_default --link  postgres-recipemountain:database backend-test '/venv/bin/coverage' 'html' '-d' '/shared/\$filehash' 
          """          // coverage html
        }
      //   publishHTML (target : [allowMissing: false,
      //     alwaysLinkToLastBuild: true,
      //     keepAll: true,
      //     reportDir: 'reports',
      //     reportFiles: 'htmlcov/index.html, htmlcov/style.css', 
      //     reportName: 'Test coverage',
      //     reportTitles: 'Test coverage'])
      }
    }
  }  
}