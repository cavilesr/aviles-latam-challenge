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

*** In construction ***

## Part 3: Integration Testing and Critical Quality Points

*** In construction ***

## Part 4: Metrics & Monitoring

*** In construction ***

## Part 5: Alerts & SRE

*** In construction ***
