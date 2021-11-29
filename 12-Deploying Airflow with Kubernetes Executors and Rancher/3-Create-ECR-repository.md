# Create ECR Repository
- We will configure ECR repository in order to store, manage and deploy Docker container images
- An ECR can be useful in the context of a CI/CD pipeline where you will push your images containing your DAGs and update your Airflow instance with it
- Open ECR in AWS console
  - Repo name: airflow
- Once repo is created, we are able to push docker images into it
- Connect to EC2 instance
- Install AWS CLI on your terminal as per the documentation.
  - Note: Do not install on EC2 instance
- Configure AWS
```
aws2 --version
aws2 configure
```
- Open ECR Dashboard
- Click - View Push Commands
- Move to the folder - docker on your terminal
- Follow the instructions
- Build docker image as per instructions
- Check images are build
- Push docker images
- Open Repo on AWS CLI and notice that images is available
