# FastAPI and GCP Deployment - Quiz

**1. What is the purpose of using Pydantic in the FastAPI application?**
- [ ] To connect to the MLFlow server
- [ ] To provide runtime checking and validation of data structures
- [ ] To deploy the application to GCP
- [ ] To create Docker containers

<details>
  <summary>Show Answer</summary>
  
  **Correct Answer:** To provide runtime checking and validation of data structures
  
  **Description:** Pydantic is a Python library that provides runtime checking and validation of data structures. In the FastAPI application, it is used to validate the data sent to the API (request body) and to parse the response data, ensuring data integrity and type safety.
</details>

---

**2. Which function is used to load a model from the MLFlow server in the predict.py file?**
- [ ] mlflow.load_model()
- [ ] mlflow.get_model()
- [ ] mlflow.pyfunc.load_model()
- [ ] mlflow.sklearn.load_model()

<details>
  <summary>Show Answer</summary>
  
  **Correct Answer:** mlflow.pyfunc.load_model()
  
  **Description:** The `mlflow.pyfunc.load_model()` function is used to load the model from the MLFlow server. It uses the model name and stage (Production) to construct the model URI and load the model for making predictions.
</details>

---

**3. What is the purpose of creating an Artifact Registry in GCP?**
- [ ] To store virtual machine configurations
- [ ] To act as a private Docker registry for storing Docker images
- [ ] To monitor application performance
- [ ] To manage firewall rules

<details>
  <summary>Show Answer</summary>
  
  **Correct Answer:** To act as a private Docker registry for storing Docker images
  
  **Description:** An Artifact Registry is a private Docker registry in GCP. It is used to store Docker images for applications and services, allowing you to push and pull container images securely within your GCP project.
</details>

---

**4. Why do we need to create a firewall rule when deploying to Compute Engine?**
- [ ] To encrypt the Docker images
- [ ] To allow traffic to port 9696 where the API is running
- [ ] To authenticate users accessing the VM
- [ ] To enable Cloud Run services

<details>
  <summary>Show Answer</summary>
  
  **Correct Answer:** To allow traffic to port 9696 where the API is running
  
  **Description:** A firewall rule is needed to allow incoming traffic (Ingress) to port 9696, which is where the FastAPI application is running. Without this rule, external requests would be blocked by GCP's default firewall settings.
</details>

---

**5. What is the main difference between Cloud Run and Compute Engine for deploying applications?**
- [ ] Cloud Run only supports Python applications
- [ ] Cloud Run is serverless and autoscaling, while Compute Engine requires manual VM management
- [ ] Compute Engine is cheaper than Cloud Run
- [ ] Cloud Run cannot run Docker containers

<details>
  <summary>Show Answer</summary>
  
  **Correct Answer:** Cloud Run is serverless and autoscaling, while Compute Engine requires manual VM management
  
  **Description:** Cloud Run is a managed, serverless platform that automatically scales up and down based on demand and abstracts away infrastructure management. Compute Engine requires you to manually set up and manage virtual machines. Cloud Run can also scale down to zero when there are no requests, making it cost-effective.
</details>

---

**6. What setting in Cloud Run makes it scale down to zero when there are no requests?**
- [ ] Allow unauthenticated invocations
- [ ] Maximum number of instances set to 1
- [ ] CPU is only allocated during request processing
- [ ] Container port set to 9696

<details>
  <summary>Show Answer</summary>
  
  **Correct Answer:** CPU is only allocated during request processing
  
  **Description:** The "CPU is only allocated during request processing" setting allows Cloud Run to scale down to zero instances when there are no incoming requests. This is the most cost-effective option as you only pay for actual request processing time.
</details>

---

**7. What command is used to push a Docker image to the Artifact Registry?**
- [ ] docker push europe-west3-docker.pkg.dev/...
- [ ] docker buildx build --platform linux/amd64 --push -t europe-west3-docker.pkg.dev/...
- [ ] gcloud docker push europe-west3-docker.pkg.dev/...
- [ ] docker deploy europe-west3-docker.pkg.dev/...

<details>
  <summary>Show Answer</summary>
  
  **Correct Answer:** docker buildx build --platform linux/amd64 --push -t europe-west3-docker.pkg.dev/...
  
  **Description:** The `docker buildx build` command with the `--push` flag builds the Docker image for the linux/amd64 platform and immediately pushes it to the specified Artifact Registry location. This single command combines building and pushing the image.
</details>