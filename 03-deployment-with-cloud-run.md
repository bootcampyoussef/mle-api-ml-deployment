# Cloud Run

**Cloud Run** is a **managed compute platform** that lets you run containers directly on top of Google's scalable infrastructure. So you don't have to set up the Cloud Engine VM yourself. Cloud Run is **serverless**, meaning that it abstracts away all infrastructure management. It is also **autoscaling**, meaning that it scales up and down automatically depending on the number of requests. And it is **fully managed**, meaning that you don't have to worry about the underlying infrastructure.

On Cloud Run, your code can either run continuously as a service or as a job. Both services and jobs run in the same environment and can use the same integrations with other services on Google Cloud.

- **Cloud Run services**. Used to run code that responds to web requests, or events.
- **Cloud Run jobs**. Used to run code that performs work (a job) and quits when the work is done.

Because we want to run a **web server**, we'll be using Cloud Run services.

## Create a Cloud Run Service

To create a Cloud Run service, click the "Navigation menu" button in the top left corner of the console, and then click "Cloud Run". Then click "Create Service".

Under `Deploy one revision from an existing container image` choose the **Docker image** that we uploaded to the **Artifact Registry**. It should be `europe-west3-docker.pkg.dev/<project-id>/docker-registry/ml-webservice:latest`. Replace `<project-id>` with the ID of the project that you want to use.

In the next step, we'll configure the service. We'll choose **`CPU is only allocated during request processing`** this means the service will **scale down to zero** when there are no requests. This is the most cost-effective option. 

The **`maximum number of instances`** is the maximum number of instances that can be created to handle requests. We'll set this to 1. This is the most cost-effective option.

And under **`Authentication`** we'll choose **`Allow unauthenticated invocations`**. This means that anyone can access the service. You could set up authentication, but that's outside the scope of this tutorial.

In the `Container, Networking, Security` section. We have to change the following settings:

Container:
- **Container port**: `9696`
- **Add Variable**: name: MLFLOW_TRACKING_URI value: <your mlflowuri>

Now we can click "Create".

If the **deployment** is successful, click on the service and you should see a **Web URL** next to the name, which will take you to the web server.
