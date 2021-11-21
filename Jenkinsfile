pipeline {
  options {
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  }
  agent {
    docker { image 'ubuntu:20.04' }
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
          sudo apt-get update
          sudo apt-get install \
          ca-certificates \
          curl \
          gnupg \
          lsb-release
          curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
          echo \
          "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
          $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
          sudo apt-get update
          sudo apt-get install docker-ce docker-ce-cli containerd.io
          
          cd services/backend
          docker build --target=test  -t backend-test .
          docker run -it backend-test '/venv/bin/pytest'
          docker run -it backend-test '/venv/bin/black' '--check' '--diff' '--verbose'  '.' 
 
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