# quytn7-devops-capstone
### Project Overview
Hello guy, I am Quy. I introduce the project with build and deploy using the Ci/Cd Jenkins platform.It integrates the process to saves time and costs. In this project, You can choice more method to deploy microservice using CircleCi or Jenkins. And Appling the method blue/green deployment or rolling deployment.

Here is the project, I create the guideline to build 1 microservice using Jenkins pipeline

### Production by me
http://a663b1753e8a544e3abbe8404a9c156b-1651972586.us-east-1.elb.amazonaws.com:8000/
### Structure and File Summary
```
.
├── Dockerfile # Dockerfile for the application
├── Jenkinsfile # Jenkins file for the CI/CD deployment
├── Makefile # Using for install and lint test
├── README.md
├── app.py # Flask run the application
├── blue_green_app
│   ├── blue_controller.json # File deploy blue controller
│   ├── blue_green_service.json # File deploy blue-green-service
│   ├── green_controller.json # File deploy green controller
│   ├── run-kubernet-blue.sh # file shell to apply controller 
│   ├── run-kubernet-green.sh # file shell to apply controller 
│   └── run-kubernet-service.sh # file shell to apply service 
├── build-cluster
│   ├── eks-cluster.yaml #create cluster using CF
│   └── eks-nodegroup.yaml #create node using CF
└── requirements.txt  # Python requirements library packages need to install
```
### Prerequisites
- AWS
- Github
- Docker

### Tools
- EC2
- Git
- Python (Flask)
- Jenkins
- Cloudformation
- AWS Elastic Kubernetes Service

### Installation Dependencies
1. Create EC2 with image Ubuntu
2. install jenkins
```
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```
3. Install plugin Jenkins
- Blue Ocean
- CloudBees Docker Build and Publish
- Docker Pipeline
- Pipeline: AWS Steps
4. Install docker
```
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
5. Install Hadolint
```
sudo wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64
sudo chmod +x /bin/hadolint
```
6. Install Kubectl
```
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
```

### Run project
1. deploy eks service and controller
```
kubectl apply -f blue_controller.json
kubectl apply -f green_controller.json
kubectl apply -f blue_green_service.json
```
2. check command eks
```
kubectl get nodes
kubectl logs podname
kubectl get services
```
### Wiki
- https://www.jenkins.io/doc/book/installing/linux/
- https://docs.docker.com/engine/install/ubuntu/
- 
