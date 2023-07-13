# Deploy a Machine Learning Model with FastAPI and Docker

You can use an Application Programming Interfaces (API) as an Endpoint to a Machine Learning model. This allows you to deploy your model and make it available to other applications. In this tutorial, you will learn how to deploy a Machine Learning model with FastAPI and Docker.

APIs are a set of protocols and tools that allow different software applications to communicate with each other. They have become an essential part of modern software development, enabling developers to build complex systems that integrate with other applications seamlessly.

FastAPI is a Python-based web framework that has gained popularity among developers for its speed, simplicity, and easy-to-use API building capabilities. It leverages the latest Python features and best practices to provide a fast, scalable, and reliable API framework.

Docker is a containerization platform that allows you to package your application and its dependencies into a single image. This makes it easy to deploy your application on any platform without worrying about compatibility issues or dependency conflicts.

## Prerequisites

To follow along with this tutorial, you will need Docker installed on your machine. You can download Docker Desktop for Mac from the official website.

Also your MLFlow server should be running. So if you stopped the SQL Server in GCP, you need to start it again first, than the Compute Engine and in the end the MLFlow for that you need to ssh into the Compute Engine and run the following command:

```bash
source mlflow/bin/activate
mlflow server \
 -h 0.0.0.0 \
 -p 5000 \
 --backend-store-uri postgresql://<db-user>:<db-password@<db-private-ip>:5432/<db-name> \
 --default-artifact-root gs://<gcs bucket>/<folder>
```


### Install the GCP SDK CLI

The GCP SDK is a set of tools that you can use to manage resources and applications hosted on GCP. You can install the GCP SDK on your local machine, or you can use the GCP console.

To install the GCP SDK on your local machine, go to [https://cloud.google.com/cli](https://cloud.google.com/cli) and follow the instructions for your operating system.

For macOS, you can install the GCP SDK by running the following command in your terminal:

```bash
brew cask install google-cloud-sdk
```



## Environment 

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
