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
      stage('Update config'){
        steps{
          withAWS(region:'us-east-1',credentials:'aws-secret'){
            sh 'aws eks update-kubeconfig --name quytn7 --region us-east-1'
        }
      }
    }
      stage('Deploy Blue System to EKS cluster'){
        steps{
          withAWS(region:'us-east-1',credentials:'aws-secret'){
            sh 'kubectl get svc'
            sh 'chmod 775 ./blue_green_app/run-kubernet-blue.sh'
            sh 'cd blue_green_app && ./run-kubernet-blue.sh '
        }
      }
    }
      stage('Deploy Green System to EKS cluster'){
        steps{
          withAWS(region:'us-east-1',credentials:'aws-secret'){
            sh 'chmod 775 ./blue_green_app/run-kubernet-green.sh'
            sh 'cd blue_green_app && ./run-kubernet-green.sh '
        }
      }
    }
      stage('Deploy Blue-Green Service to EKS cluster'){
        steps{
          withAWS(region:'us-east-1',credentials:'aws-secret'){
            sh 'chmod 775 ./blue_green_app/run-kubernet-service.sh'
            sh 'cd blue_green_app && ./run-kubernet-service.sh '
        }
      }
    }
      stage("Cleaning up") {
          steps{
              sh 'sudo docker system prune --force'
          }
       }
  }
}