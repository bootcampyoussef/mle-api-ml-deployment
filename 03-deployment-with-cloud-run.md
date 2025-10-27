# Cloud Run

**Cloud Run** is a **managed compute platform** that lets you run containers directly on top of Google's scalable infrastructure. So you don't have to set up the Cloud Engine VM yourself. Cloud Run is **serverless**, meaning that it abstracts away all infrastructure management. It is also **autoscaling**, meaning that it scales up and down automatically depending on the number of requests. And it is **fully managed**, meaning that you don't have to worry about the underlying infrastructure.

On Cloud Run, your code can either run continuously as a service or as a job. Both services and jobs run in the same environment and can use the same integrations with other services on Google Cloud.

- **Cloud Run services**. Used to run code that responds to web requests, or events.
- **Cloud Run jobs**. Used to run code that performs work (a job) and quits when the work is done.

Because we want to run a **web server**, we'll be using Cloud Run services.

## Create a Cloud Run Service

To create a Cloud Run service, click the **Navigation menu** button in the top left corner of the console, and then click **Cloud Run**. Then click **Services**. Once in **Services** click on **+ Deploy container**.

- Keep checked the `Deploy one revision from an existing container image`.
- Select the **Container image URL** that we uploaded to the **Artifact Registry** from the rigth pop-up window. It should be `europe-west3-docker.pkg.dev/<project-id>/docker-registry/ml-webservice@sha256:<some digit numeber>`. Replace `<project-id>` with the ID of the project that you want to use.
- Under **Configure**:
  - **Service name**: `ml-webservice`
  - **Region**: `europe-west3`
  - **Authentification**: `Allow public access`  This means that anyone can access the service. You could set up authentication, but that's outside the scope of this tutorial.
  - **Billing**: `Requested-based`
  - **Service scaling**:
    - **Auto scaling**
    - **Minimum number of instances**: `1`
    - **Maximum number of instances**: `1` 
The **`maximum number of instances`** is the maximum number of instances that can be created to handle requests. We'll set this to 1. This is the most cost-effective option.


In the `Containers, Volumes, Networking, Security` section. We have to change the following settings:

**Containers**:
- **Container port**: `9696`
- **Variables & Secrets**:
  - Click on **Add Variable**
- **Add Variable**:
    - **Name 1**: `MLFLOW_TRACKING_URI` 
    - **Value 1**: `<your mlflowuri>`


Now we can click **Create**.

If the **deployment** is successful, click on the service and you should see a **Web URL** next to the name, which will take you to the web server.
