pipeline{
  agent any
  environment {
        registryCredential = "dockerhub"
        dockerImage = ""
        PATH="$HOME/.local/bin:$PATH"
    }
  stages{
      stage('Install dependencies from Makefile'){
        steps{
          sh 'make install'
        }
      }
      stage('Lint code'){
        steps{
            sh 'make lint'
        }
      }
      stage('Build docker image'){
        steps{
          script{
            docker.withRegistry("", registryCredential){
              dockerImage = docker.build "trangocquy123/quytn7-capstone1"
            }
          }
        }
      }
      stage('Push image'){
        steps{
          script{
            docker.withRegistry("", registryCredential){
              dockerImage.push()
            }
          }
        }
      }
      stage('Deploy Blue System to EKS cluster'){
        steps{
          withAWS(region:'us-east-1',credentials:'aws-secret'){
            sh 'cd blue_green_app && kubectl apply -f blue_controller.json'
        }
      }
    }
      stage('Deploy Green System to EKS cluster'){
        steps{
          withAWS(region:'us-east-1',credentials:'aws-secret'){
            sh 'cd blue_green_app && kubectl apply -f green_controller.json'
        }
      }
    }
      stage('Deploy Blue-Green Service to EKS cluster'){
        steps{
          withAWS(region:'us-east-1',credentials:'aws-secret'){
            sh 'cd blue_green_app && kubectl apply -f blue_green_service.json'
        }
      }
    }
  }
}