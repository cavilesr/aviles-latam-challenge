# aviles-latam-challenge
## Objective
This repository contains a system designed for ingesting and storing data in a database, enabling advance analytics. It also includes an HTTP API for exposing the data, allowing third-party consumption.

## Part 1: Insfrastructure and IaC
### Requirements
```
1. Identify the necessary infrastructure to ingest, store and expose data:
    1. Use the Pub/Sub Schema for data ingestion.
    2. Database for storage focused on data analytics.
    3. HTTP Endpoint to serve a portion of the stored data
```
One of the simplest and easiest options for implementing the system would be to use the following technologies:

1. For data ingestion of the Pub/Sub pattern: Apache Kafka
    - Apache Kafka is a widely adopted open-source distributed streaming platform known for its scalability, fault-tolerance, and reliable message delivery. It provides strong durability guarantees and supports high-throughput data ingestion, making it suitable for handling large volumes of data in a resilient manner.
2. For data storage: Elasticsearch
    - Elasticsearch is a highly scalable and distributed search and analytics engine. It is designed for real-time data analysis and provides powerful querying capabilities. With its ability to handle large amounts of structured and unstructured data, Elasticsearch is well-suited for storing and indexing data for advanced analytics use cases.
3. For data exposition: Flask
    - Flask is a lightweight and flexible Python web framework that allows you to quickly build HTTP endpoints. It provides a simple and intuitive interface for creating RESTful APIs. Flask's simplicity and extensibility make it a suitable choice for exposing data through an HTTP API.

While this combination of technologies can provide a straightforward solution for data ingestion, storage, and exposition, it's important to note that they are not inherently cloud-native. To ensure a more cloud-native approach, it is recommended to leverage the tools available directly in the cloud environment. For example:

1. For data ingestion: Google Cloud Pub/Sub
    - Google Cloud Pub/Sub is a fully managed, scalable, and reliable messaging service. It offers durable message storage, guaranteed delivery, and supports high throughput. Cloud Pub/Sub integrates seamlessly with other Google Cloud services, making it an ideal choice for building cloud-native applications.
2. For data storage: Google Cloud BigQuery
    - Google BigQuery is a fully managed, serverless data warehouse designed for analytics workloads. It offers high-performance querying, automatic scaling, and built-in support for handling large datasets. BigQuery's integration with other Google Cloud services, such as Pub/Sub, allows for seamless data ingestion and analytics workflows.
3. For data exposition: Google Cloud Run
    - Google Cloud Run is a fully managed serverless compute platform that allows you to run stateless containers. It automatically scales based on incoming request traffic and provides a secure and isolated execution environment. Cloud Run is well-suited for deploying HTTP endpoints as it abstracts away infrastructure management and provides scalability and resilience out of the box.

By leveraging these cloud-native technologies, the system can benefit from seamless integration, scalability, and easier configuration. This approach ensures better compatibility with the cloud environment and facilitates future scalability and integration with other cloud services.

## Part 2: Applications and CI/CD flow
### Requirements
```
1. Set up and HTTP Endpoint with logic to read data from a database and expose it upon receiving a GET request.

2. Deploy the HTTP API to the cloud using CI/CD. Workflow and executions should be visible in the repository.

3. Include an architecture diagram
```
In order to setup correctly the HTTP endpoint as required, the following files were elaborated:
1. [Requirements](/requirements.txt)
    - This file lists the dependencies required for the Python code to run. It includes the Flask framework for building the HTTP endpoint and the google-cloud-bigquery library for interacting with Google Cloud BigQuery.
2. [Python code](/main.py)
    - This file contains the Python code that defines the HTTP endpoint. It includes a route that listens for GET requests and retrieves data from the specified BigQuery table in JSON format.
3. [Dockerfile](/Dockerfile)
    - This file is used to build a Docker image.
4. [Jenkinsfile](/jenkinsfile)
    - This file defines the CI/CD pipeline using Jenkins. It includes stages to checkout the source code for changes, building the Docker image and deploying the image to Google Cloud Functions.

### Architectural Diagram
![Architectural diagram](/assets/images/diagram.png)

The architectural diagram can be described as follows:
1. User interface: The user interacts with the system by sending HTTP GET resquests to the exposed endpoints
2. Flask Application: The Flask framework is used to build the HTTP endpoint within the Cloud Function. It handles the incoming requests, retrieves data from Google Cloud BigQuery, and returns the data as a JSON response.
3. Cloud Run: The HTTP endpoint is implemented as a serverless service using Google Cloud Run. It receives the GET requests and triggers the execution of the associated code.
4. Google Cloud BigQuery: The system leverages Google Cloud BigQuery as the data storage and retrieval mechanism. It stores the structured data in a table, and the Flask application queries the table to retrieve the required data.
5. Docker: The system utilizes Docker to containerize the Flask application. The Dockerfile specifies the necessary dependencies, builds the Docker image, and packages the application along with its dependencies.
6. Artifact Registry: The Docker image is pushed to a container registry, such as Google Artifact Registry (GAR). The registry stores the Docker image and makes it available for deployment.
7. Jenkins: The CI/CD pipeline is orchestrated using Jenkins. Jenkins is responsible for automating the build, test, and deployment processes. It pulls the source code from the version control system, builds the Docker image, and deploys the image to Google Artifact Registry and then is built into Google Cloud Run.

## Part 3: Integration Testing and Critical Quality Points
### Requirements
```
1. Implement an integration test in the CI/CD pipeline to verify that the API effectively exposes data from the database. Provide arguments for this test.

2. Propose other integration tests to validate that the system is functioning correctly and explain how they would be implemented.

3. Identify possible critical points in the system (in terms of failure or performance) that are different from the previous point and suggest ways to test or measure them (without implementing).

4. Propose technical measures to strengthen the system and address or resolve these critical points.
```

## Part 4: Metrics & Monitoring

*** In construction ***

## Part 5: Alerts & SRE

*** In construction ***
