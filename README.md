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
In these [Integration tests](/integration_tests.py), I defined the following test cases:
1. The **test_get_data** method, which sends a GET request to the API endpoint and asserts that the response status code is 200 (OK).
2. The **test_insert_data** method, which sends a payload with a POST request to the API endpoint, asserts that the response status code is 200 (OK) and then validates that the inserted data is reflected in a subsequent GET request.
3. The **test_update_data** method, which sends a payload with a PUT request to the API endpoint, asserts that the response status code is 200 (OK) and then validates that the updated data is reflected in a subsequent GET request.

Other integration tests to validate that the system is working correctly could include:
- **Testing error handling**: These are tests that simulate wrong requests or invalid data to ensure that the API handles them correctly, returning appropriate error responses.
- **Testing performance**: These are tests that measure the response time of the API using different load conditions, such as sending multiple concurrent requests or gradually increasing the number of requests.

Some possible critical points in the system could be:
- **Database connection failures**. A way to test the system's resilience to database connection failures could be by simulating scenarios where the database becomes temporaly unavailable or experiences high latency.
- **Scalability and performance**. This could be measured by simulating a high number of concurrent requests and monitoring responses times and resources utilization.
- **Error handling**. This could be achieved by testing the system with large data sets, invalid or malformed requests and unexpected inputs, to ensure it correctly handles errors and does not crash or expose sensitive information.

Having identified these critical points, some technical measures that could be implemented to strengthen the system are:
- **Caching**: Introducing caching mechanisms to reduce the load on the database and improve response times for frequently accessed data.
- **Load testing and performance optimization**: Implementing load testing to identify performance bottlenecks and optimize the system accordingly. This may involve optimizing database queries, improving indexing or scaling up resources.
- **Monitoring and Logging**: Implement comprenhensive monitoring and logging solutions (as the ones that are native already to GCP) to track system performance, identify issues, and facilitate troubleshooting. This can include monitoring database performance, API response times, error rates, among others.

## Part 4: Metrics & Monitoring
### Requirements
```
1. Propose 3 metrics (besides CPU/RAM/DISK USAGE) critical to understand the health and performance of the end-to-end system.

2. Propose a visualization tool and describe the  metrics it would display and how this information would help us understand the system's health for making strategic decisions.

3. Describe how the implementation would be in the cloud and how it would collect system metrics.

4. Describe how the visualization would change if we scale the solution to 50 similar systems and what other metrics or visualization methods would unlock this scalability.

5.Comment on the difficulties or limitations that could arise in terms of system observability if the scalability problem is not addressed correctly.
```


## Part 5: Alerts & SRE

*** In construction ***
