# Deploy Krikey-Greeting API to Google Kubernetes Engine (GKE)

## 1. Background
* Krikey-Greeting is a REST API end-point developed in nodejs, using restify library.
* This service is packaged as a Docker container. Its image is hosted in Docker Hub
 (https://hub.docker.com/repository/docker/blublud/krikey-greeting)
* Source code and related materials can be founded in this github repo (???) 

## 2. Deploy Krikey-Greeting
Once Krikey-Greeting docker image is published to a repository (in this case Docker Hub),
one can deploy it to a GKE.

* Preparing GKE environment
This prerequisite consists of creating GKE project, GKE cluster, setting Gooogle Cloud Shell.
Instruction for this step can be found here (https://cloud.google.com/shell/docs/quickstart?hl=en_US)  

* Obtaining kubernetes resource specs (.yaml files): within GCS,
`git clone ???`

* Creating a Deployment for Krikey-Greeting service
`kubectl create -f krikey-greeting-deployment.yaml`

* Creating a Service for Krikey-Greeting Deployment
`kubectl create -f krikey-greeting-service.yaml`

* Test if Deployment and Service are successfully created
Determine cluster IP address assigned to krikey-greeting Service 
(line krikey-greeting, column CLUSTER-IP):
`kubectl get svc`

Find a pod within kubernetes cluster:
`kubectl get pod`
Pick a pod having prefix *krikey-greeting*-xxx  (for example, krikey-greeting-5f98df9778-xzbf6).

Enter the container's shell 
`kubectl exec -it krikey-greeting-5f98df9778-xzbf6 -- ash`
Install curl command if necessary (curl command is used to test krikey-greeting service)
`apk add curl`

Send a GET HTTP request to krikey-greeting service
`curl http://<SERVICE-CLUSTER-IP-ADDRESS>/greetings?name=Krikey`
A correct response should be
`{"greeting":"Hello Krikey"}`
