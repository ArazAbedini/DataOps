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

             +------------------+
             |  JSON Data File  |
             +--------+---------+
                      |
               [Python Producer]
                      |
                 Kafka Topic
                      |
                  Logstash
     +----------------+---------------+
     | Transformation, Validation, etc|
     +----------------+---------------+
                      |
                Elasticsearch
                      |
                    Kibana

## Input and Output:
