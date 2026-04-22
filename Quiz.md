# Local FastAPI and MLflow Deployment - Quiz

**1. What is the purpose of using Pydantic in the FastAPI application?**

- [ ] To connect to the MLFlow server
- [ ] To provide runtime checking and validation of data structures
- [ ] To deploy the application to a remote cloud platform
- [ ] To create Docker containers

<details>
  <summary>Show Answer</summary>

  **Correct Answer:** To provide runtime checking and validation of data structures

  **Description:** Pydantic is a Python library that provides runtime checking and validation of data structures. In the FastAPI application, it is used to validate the data sent to the API (request body) and to parse the response data, ensuring data integrity and type safety.
</details>

---

**2. Which function is used to load a model from the MLflow Model Registry in the `predict.py` file?**

- [ ] mlflow.load_model()
- [ ] mlflow.get_model()
- [ ] mlflow.pyfunc.load_model()
- [ ] mlflow.sklearn.load_model()

<details>
  <summary>Show Answer</summary>

  **Correct Answer:** mlflow.pyfunc.load_model()

  **Description:** The `mlflow.pyfunc.load_model()` function is used to load the registered model. In this repo, the API loads the model by name and alias from the local MLflow Model Registry.
</details>

---

**3. What is the role of the local MLflow tracking server in this repo?**

- [ ] It only hosts the FastAPI application
- [ ] It stores experiment runs, registered models, and model artifacts locally
- [ ] It replaces Docker Desktop
- [ ] It validates Pydantic schemas

<details>
  <summary>Show Answer</summary>

  **Correct Answer:** It stores experiment runs, registered models, and model artifacts locally

  **Description:** The local MLflow server tracks runs, stores logged artifacts, and exposes the Model Registry that the FastAPI service reads from when loading the production model.
</details>

---

**4. Why does the API convert a single request into a one-row table before calling `model.predict()`?**

- [ ] Because FastAPI only supports table inputs
- [ ] Because MLflow pyfunc models typically expect tabular input
- [ ] Because Pydantic requires a pandas DataFrame
- [ ] Because Docker needs CSV-style payloads

<details>
  <summary>Show Answer</summary>

  **Correct Answer:** Because MLflow pyfunc models typically expect tabular input

  **Description:** Even when you send only one prediction request, MLflow pyfunc models usually expect a tabular structure such as a pandas DataFrame. The API wraps the engineered features into a single-row table before calling the model.
</details>

---

**5. What is the purpose of the `production` alias in the Model Registry?**

- [ ] It renames the FastAPI route
- [ ] It marks which registered model version the API should load
- [ ] It creates a Docker image tag
- [ ] It starts the MLflow server

<details>
  <summary>Show Answer</summary>

  **Correct Answer:** It marks which registered model version the API should load

  **Description:** Aliases let you point the API at a stable name such as `production` instead of hard-coding a specific version number. That makes model promotion easier when you register a new version later.
</details>

---

**6. Why is Docker treated as optional in the revamped workflow?**

- [ ] Because Docker cannot run Python
- [ ] Because the recommended order is to validate the local Python workflow first
- [ ] Because MLflow does not work in containers
- [ ] Because a notebook editor replaces Docker

<details>
  <summary>Show Answer</summary>

  **Correct Answer:** Because the recommended order is to validate the local Python workflow first

  **Description:** Local development is easier to debug directly in Python. Once the notebook, MLflow server, and API work together locally, packaging the API in Docker becomes much easier to reason about.
</details>

---

**7. What should you select as the notebook kernel before running the model-registration notebook?**

- [ ] The local MLflow server process
- [ ] The `.venv` Python environment created during setup
- [ ] Docker Desktop
- [ ] The registered model alias

<details>
  <summary>Show Answer</summary>

  **Correct Answer:** The `.venv` Python environment created during setup

  **Description:** The notebook should run with the same Python environment where the project dependencies were installed. That keeps MLflow, scikit-learn, pandas, and the environment-loading helpers available to the notebook.
</details>
