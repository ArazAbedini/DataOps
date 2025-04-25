# DataOps

# DataOps Pipeline with Kafka, Logstash, Elasticsearch, and Kibana

This project is a DataOps pipeline that ingests messy JSON data via Kafka, cleans and normalizes it using Logstash, and stores it into Elasticsearch for visualization through Kibana.

---

## Key features

- Raw, messy JSON records.
- Use Kafkaas the buffer.
- Logstash filters, transforms, and validates of data.
- Elasticsearch indexes act as  storage.
- Kibana is used to monitor the final output.

---

- **Kafka + Zookeeper**: Message broker.
- **Python Kafka Producer**: Publishes sample data.
- **Logstash**: Cleans and transforms the messages.
- **Elasticsearch**: Stores structured, searchable data.
- **Kibana**: Visualizes processed data.

---

## Architecture

flowchart LR
    [JSON Data File] --> [Python Producer] --> [Kafka Topic] --> [Logstash Pipeline] --> [Elasticsearch Index] --> [Kibana Dashboard]

## Input and Output:

- Input sample:
  
[
  {
    "id": "123",
    "full_name": "Ali",
    "timestamp": "2025/01/31 12:34:56",
    "active": "true"
  },
  {
    "id": "124",
    "full_name": " ",
    "timestamp": "2025-01-31T14:20:00Z",
    "active": "false",
    "extra_field": "i should be removed!"
  }
]

- Output sample:

[
  {
    "id": 123,
    "name": "Ali",
    "timestamp": "2025-01-31T12:34:56Z",
    "active": true
  },
  {
    "id": 124,
    "name": null,
    "timestamp": "2025-01-31T14:20:00Z",
    "active": false
  }
]

## Features

- Only valid data is stored

- All unwanted fields are removed

- Availabilty for multiple timestamp formats

- Partitioned Kafka publishing

- Deployment with docker-compose

## Challenges

 - Handling multiple timestamp formats --> Handling with logStash
 - Avoid Kafka race in situation which producer wants to ingest data before topic is created --> Handling with health check
 - Field Normalaztion --> Handling with Logstahs 
 - Avoid race among services --> Handling with depends on in docker-compose
 - Uncertainty About stages --> Handling with Logs monitoring each step
 - Slow filtering --> Handling with additional consumer in logstash 
 - Parallelism --> Handling with Adding more Partition to solve 

 ## Improvements
  
  - Add unit tests for the producer.

  - Use Kafka Connect formore scalable ingestion.

  - Stream process while data ingested do pipeline

  - Increase number of producer for parallelism
  
  - Increase replication factor for improving stability  




