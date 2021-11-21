pipeline {
  options {
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  }
  agent {
    docker { image 'python:3.9-alpine' }
  }
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
          cd service/backend
          pip install -r requirements.txt
          pip install coverage
          """
        }
      }
    }
    stage('Linting') { // Run pylint against your code
      steps {
        script {
          sh """
          black --check .
          """
        }
      }
    }
    stage('Unit Testing') { // Perform unit testing
      steps {
        script {
          sh """
          pytest --junitxml=report.xml
          """
        }
      }
    }
    stage('Test coverage') { // Perform unit testing
      steps {
        script {
          sh """
          coverage run -m pytest
          coverage html
          """
        }
        publishHTML (target : [allowMissing: false,
          alwaysLinkToLastBuild: true,
          keepAll: true,
          reportDir: 'reports',
          reportFiles: 'htmlcov/index.html, htmlcov/style.css', 
          reportName: 'Test coverage',
          reportTitles: 'Test coverage'])
      }
    }
  }  
}