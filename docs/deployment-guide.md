# CloudPulse Deployment Guide

This guide provides step-by-step instructions for deploying CloudPulse to Amazon EKS (Elastic Kubernetes Service).

## Prerequisites

Before you begin, ensure you have the following:

- AWS CLI installed and configured with appropriate credentials
- kubectl installed
- Docker installed
- eksctl installed

## Step 1: Create an Amazon EKS Cluster

1. Create an EKS cluster using eksctl:

```bash
eksctl create cluster \
--name cloudpulse-cluster \
--region us-east-1 \
--nodegroup-name standard-workers \
--node-type t3.medium \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4 \
--managed
```

2. Verify the cluster is running:

```bash
kubectl get nodes
```

## Step 2: Set Up Amazon ECR

1. Create an ECR repository:

```bash
aws ecr create-repository --repository-name cloudpulse --region us-east-1
```

2. Note the repository URI from the output.

## Step 3: Build and Push Docker Image

1. Build your Docker image:

```bash
docker build -t cloudpulse .
```

2. Tag the image with your ECR repository URI:

```bash
docker tag cloudpulse:latest <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/cloudpulse:latest
```

3. Log in to ECR:

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.us-east-1.amazonaws.com
```

4. Push the image to ECR:

```bash
docker push <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/cloudpulse:latest
```

## Step 4: Deploy to Kubernetes

1. Create a Kubernetes deployment YAML file (`cloudpulse-deployment.yaml`):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudpulse
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cloudpulse
  template:
    metadata:
      labels:
        app: cloudpulse
    spec:
      containers:
      - name: cloudpulse
        image: <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/cloudpulse:latest
        ports:
        - containerPort: 5000
```

2. Apply the deployment:

```bash
kubectl apply -f cloudpulse-deployment.yaml
```

3. Create a Kubernetes service YAML file (`cloudpulse-service.yaml`):

```yaml
apiVersion: v1
kind: Service
metadata:
  name: cloudpulse-service
spec:
  selector:
    app: cloudpulse
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: LoadBalancer
```

4. Apply the service:

```bash
kubectl apply -f cloudpulse-service.yaml
```

## Step 5: Access Your Application

1. Get the external IP of your service:

```bash
kubectl get services cloudpulse-service
```

2. Use the EXTERNAL-IP to access your application in a web browser.

## Troubleshooting

- If pods are not starting, check the logs:

```bash
kubectl logs <pod-name>
```

- To check the status of your deployments:

```bash
kubectl get deployments
```

- If you need to update your deployment with a new image:

```bash
kubectl set image deployment/cloudpulse cloudpulse=<your-account-id>.dkr.ecr.us-east-1.amazonaws.com/cloudpulse:new-tag
```

## Cleaning Up

To avoid incurring unnecessary costs, remember to delete your resources when you're done:

1. Delete the Kubernetes resources:

```bash
kubectl delete service cloudpulse-service
kubectl delete deployment cloudpulse
```

2. Delete the EKS cluster:

```bash
eksctl delete cluster --name cloudpulse-cluster --region us-east-1
```

3. Delete the ECR repository:

```bash
aws ecr delete-repository --repository-name cloudpulse --force --region us-east-1
```

Remember to replace `<your-account-id>` with your actual AWS account ID throughout this guide.
